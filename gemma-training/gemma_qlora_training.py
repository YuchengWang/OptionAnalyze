import os
import sys
import json
import numpy as np
import gc
import shutil
import time
from dotenv import load_dotenv

# --- 1. GLOBAL SYSTEM CONFIGURATION ---
os.environ["XLA_PYTHON_CLIENT_PREALLOCATE"] = "false"
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = ".80"
os.environ["XLA_PYTHON_CLIENT_ALLOCATOR"] = "platform"

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

import jax
import jax.numpy as jnp
import optax
import qwix
from flax import nnx
from huggingface_hub import snapshot_download, login
from tunix.models.gemma3 import model as gemma3_model_lib
from tunix.models.gemma3 import params_safetensors as params_safetensors_lib
from tunix.sft import peft_trainer, utils
from tunix.generate import tokenizer_adapter as tokenizer_lib
from tunix.generate import sampler as sampler_lib

# --- 2. DYNAMIC CONFIGURATION ---
MODEL_ID = "google/gemma-3-1b-it"
TRAIN_FILE = "outputs/imf_train.jsonl"
CHECKPOINT_DIR = "outputs/gemma3_lora_results"

# Precision parameters
LEARNING_RATE = 1e-5 
LORA_RANK = 8        
MAX_SEQ_LEN = 768
CACHE_SIZE = 1024   
NUM_EPOCHS = 1       # Exactly 1 pass over the data to avoid repetition

SYSTEM_MSG = "You are a specialized IMF Financial Analyst. Provide technical responses based on provided macroeconomic data."

script_dir = os.path.dirname(os.path.abspath(__file__))
train_file_path = os.path.join(script_dir, TRAIN_FILE)
abs_checkpoint_path = os.path.abspath(os.path.join(script_dir, CHECKPOINT_DIR))

# --- 3. DATA LOADING & STEP CALCULATION ---
class RefinedFinancialLoader:
    def __init__(self, file_path, tokenizer):
        self.batches = []
        pad_id = tokenizer.pad_id()
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found. Run process_imf_data.py first.")
            sys.exit(1)
            
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)
                full_text = f"<start_of_turn>system\n{SYSTEM_MSG}<end_of_turn>\n"
                full_text += f"<start_of_turn>user\n{entry['instruction']}\n{entry['input']}<end_of_turn>\n"
                full_text += f"<start_of_turn>model\n{entry['output']}<end_of_turn>"
                tokens = tokenizer.encode(full_text)
                arr = np.full((1, MAX_SEQ_LEN), pad_id, dtype=np.int32)
                ln = min(len(tokens), MAX_SEQ_LEN)
                arr[0, :ln] = tokens[:ln]
                self.batches.append(peft_trainer.TrainingInput(input_tokens=arr, input_mask=(arr != pad_id)))
    
    def __len__(self): return len(self.batches)
    def __iter__(self): return iter(self.batches * NUM_EPOCHS)

# --- 4. INFRASTRUCTURE & INITIALIZATION ---
if hf_token := os.getenv("HF_TOKEN"):
    login(token=hf_token)

if os.path.exists(abs_checkpoint_path):
    shutil.rmtree(abs_checkpoint_path)
os.makedirs(abs_checkpoint_path, exist_ok=True)

print("📦 Loading architecture and weights...")
local_model_path = snapshot_download(repo_id=MODEL_ID, ignore_patterns=["*.pth"], token=hf_token)
model_config = gemma3_model_lib.ModelConfig.gemma3_1b_it()
base_model = params_safetensors_lib.create_model_from_safe_tensors(local_model_path, model_config)

lora_provider = qwix.LoraProvider(
    module_path=".*q_einsum|.*kv_einsum|.*gate_proj|.*down_proj|.*up_proj",
    rank=LORA_RANK, alpha=LORA_RANK * 2, weight_qtype="nf4", tile_size=128,
)
model = qwix.apply_lora_to_model(base_model, lora_provider, rngs=nnx.Rngs(0), **base_model.get_model_input())
tokenizer = tokenizer_lib.Tokenizer(tokenizer_path=os.path.join(local_model_path, "tokenizer.model"))

# Load data and determine steps
dataset = RefinedFinancialLoader(train_file_path, tokenizer)
DYNAMIC_MAX_STEPS = len(dataset) * NUM_EPOCHS
EVAL_FREQ = max(1, DYNAMIC_MAX_STEPS // 2)

print(f"📊 Dataset Stats: {len(dataset)} unique chunks identified.")
print(f"⚙️ Training Plan: {DYNAMIC_MAX_STEPS} steps ({NUM_EPOCHS} epoch/s).")

# --- 5. EVALUATION UTILITY ---
def run_expert_evaluation(title, model, tokenizer, model_config):
    print(f"\n📈 --- [EVALUATION] {title} ---")
    query = "Analyze the technical outlook for global GDP growth in 2024-2025 according to the latest data."
    full_prompt = f"<start_of_turn>system\n{SYSTEM_MSG}<end_of_turn>\n"
    full_prompt += f"<start_of_turn>user\n{query}<end_of_turn>\n<start_of_turn>model\n"
    
    # Correct way to pass config parameters without using __dict__
    cache_cfg = sampler_lib.CacheConfig(
        cache_size=CACHE_SIZE, 
        num_layers=model_config.num_layers,
        num_kv_heads=model_config.num_kv_heads,
        head_dim=model_config.head_dim
    )
    sampler = sampler_lib.Sampler(transformer=model, tokenizer=tokenizer, cache_config=cache_cfg)
    results = sampler(input_strings=[full_prompt], max_generation_steps=250, eos_tokens=[tokenizer.eos_id()])
    
    response = results.text[0].split("<start_of_turn>model\n")[-1].replace("<end_of_turn>", "").strip()
    print(f"Expert Response:\n{response}\n")
    del sampler
    gc.collect()

run_expert_evaluation("PRE-TRAINING (Baseline)", model, tokenizer, model_config)

# --- 6. TRAINING ---
print(f"\n🔥 Commencing Knowledge Injection ({DYNAMIC_MAX_STEPS} steps)...")
trainer = peft_trainer.PeftTrainer(
    model=model, 
    optimizer=optax.adamw(learning_rate=optax.cosine_decay_schedule(init_value=LEARNING_RATE, decay_steps=DYNAMIC_MAX_STEPS)),
    training_config=peft_trainer.TrainingConfig(
        max_steps=DYNAMIC_MAX_STEPS, 
        eval_every_n_steps=EVAL_FREQ, 
        checkpoint_root_directory=abs_checkpoint_path
    )
).with_gen_model_input_fn(lambda x: {
    "input_tokens": x.input_tokens, "input_mask": x.input_mask,
    "positions": utils.build_positions_from_mask(x.input_mask),
    "attention_mask": utils.make_causal_attn_mask(x.input_mask),
})

trainer.train(dataset, [])
print("\n✅ Knowledge Injection Complete!")

run_expert_evaluation("POST-TRAINING (Gemma-Expert)", model, tokenizer, model_config)
