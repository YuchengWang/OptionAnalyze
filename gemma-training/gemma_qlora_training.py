import os
import sys
import json
import numpy as np
import gc
from dotenv import load_dotenv

# --- 1. 加载环境与安全检查 ---
# 建议通过 ./run_gpu_training.sh 运行以确保 GPU 库路径正确
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 导入 JAX 前设置（避免 OOM）
os.environ["XLA_PYTHON_CLIENT_PREALLOCATE"] = "false"

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

# 登录 Hugging Face
hf_token = os.getenv("HF_TOKEN")
if hf_token:
    login(token=hf_token)

# 强制 GPU 检查：如果是 Demo，我们必须确保硬件加速已启用
devices = jax.devices()
print(f"🚀 JAX 运行设备: {devices}")
if not any(d.platform == 'gpu' for d in devices):
    print("❌ 错误: 未检测到 GPU！请使用 ./run_gpu_training.sh 启动。")
    sys.exit(1)

# --- 2. 配置与数据准备 ---
MODEL_ID = "google/gemma-3-1b-it"
TRAIN_FILE = "outputs/imf_train.jsonl"
CHECKPOINT_DIR = "outputs/gemma3_lora_results"
MAX_STEPS = 150 
MAX_SEQ_LEN = 512 

script_dir = os.path.dirname(os.path.abspath(__file__))
train_file_path = os.path.join(script_dir, TRAIN_FILE)

if not os.path.exists(train_file_path):
    print(f"🔍 正在生成训练数据 {TRAIN_FILE}...")
    from process_imf_data import pdf_to_high_quality_jsonl
    pdf_file = os.path.join(script_dir, "outputs/imf_weo_2024.pdf")
    pdf_to_high_quality_jsonl(pdf_file, train_file_path)

# --- 3. 模型初始化 (Gemma-3 + QLoRA) ---
print("📦 正在加载模型权重...")
local_model_path = snapshot_download(repo_id=MODEL_ID, ignore_patterns=["*.pth"], token=hf_token)
model_config = gemma3_model_lib.ModelConfig.gemma3_1b_it()
base_model = params_safetensors_lib.create_model_from_safe_tensors(local_model_path, model_config)

print("🎨 注入 QLoRA 适配器...")
lora_provider = qwix.LoraProvider(
    module_path=".*q_einsum|.*kv_einsum|.*gate_proj|.*down_proj|.*up_proj",
    rank=8, alpha=16.0, weight_qtype="nf4", tile_size=128,
)
model = qwix.apply_lora_to_model(base_model, lora_provider, rngs=nnx.Rngs(0), **base_model.get_model_input())
tokenizer = tokenizer_lib.Tokenizer(tokenizer_path=os.path.join(local_model_path, "tokenizer.model"))

# --- 4. 训练前测试 (Baseline) ---
test_prompts = ["Summarize the global growth risks mentioned in the October 2024 IMF report."]
formatted = [f"<start_of_turn>user\n{p}<end_of_turn>\n<start_of_turn>model\n" for p in test_prompts]

def run_inference(title):
    print(f"\n📉 --- {title} ---")
    sampler = sampler_lib.Sampler(transformer=model, tokenizer=tokenizer, 
                                  cache_config=sampler_lib.CacheConfig(cache_size=256, **model_config.__dict__))
    results = sampler(input_strings=formatted, max_generation_steps=100)
    print(f"回答: {results.text[0].strip()}")
    del sampler
    gc.collect()

run_inference("训练前回答")

# --- 5. 执行微调 (Fine-tuning) ---
print("\n🔥 开始金融知识注入 (SFT)...")

class FinancialDataLoader:
    def __init__(self, file_path, tokenizer, max_length=512):
        self.batches = []
        pad_id = tokenizer.pad_id()
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)
                full_text = f"<start_of_turn>user\n{entry['instruction']}\n{entry['input']}<end_of_turn>\n"
                full_text += f"<start_of_turn>model\n{entry['output']}<end_of_turn>"
                tokens = tokenizer.encode(full_text)
                arr = np.full((1, max_length), pad_id, dtype=np.int32)
                ln = min(len(tokens), max_length)
                arr[0, :ln] = tokens[:ln]
                self.batches.append(peft_trainer.TrainingInput(input_tokens=arr, input_mask=(arr != pad_id)))
    def __len__(self): return len(self.batches)
    def __iter__(self): return iter(self.batches)

trainer = peft_trainer.PeftTrainer(
    model=model, optimizer=optax.adamw(2e-5),
    training_config=peft_trainer.TrainingConfig(
        max_steps=MAX_STEPS, checkpoint_root_directory=os.path.abspath(os.path.join(script_dir, CHECKPOINT_DIR))
    )
).with_gen_model_input_fn(lambda x: {
    "input_tokens": x.input_tokens, "input_mask": x.input_mask,
    "positions": utils.build_positions_from_mask(x.input_mask),
    "attention_mask": utils.make_causal_attn_mask(x.input_mask),
})

trainer.train(FinancialDataLoader(train_file_path, tokenizer), [])
print("\n✅ 训练完成！")

# --- 6. 训练后测试 (Results) ---
run_inference("训练后回答")
