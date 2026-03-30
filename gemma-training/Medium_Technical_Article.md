# Injecting Financial Expertise into Gemma-3: A JAX/QLoRA Engineering Deep Dive on NVIDIA T4

**By: Senior AI Research Engineer**

Fine-tuning Large Language Models (LLMs) on specialized vertical data remains one of the most challenging tasks in modern AI engineering—especially when working within the constraints of "entry-level" cloud hardware. This report documents a successful experiment in injecting the **IMF 2024 World Economic Outlook** into the **Gemma-3-1b-it** model using a JAX-native QLoRA workflow on a Google Cloud GCE instance.

---

## 1. The Infrastructure: Living on the Edge of 15GB RAM

Our lab environment was deployed on **Google Cloud Platform (GCP)** with the following specifications:
*   **Machine Type:** `n1-standard-4` (4 vCPUs, 15 GB Memory)
*   **Accelerator:** 1 x **NVIDIA Tesla T4** (16 GB GDDR6)
*   **Zone:** `us-central1-a`

**Expert Insight:** 15GB of system RAM is exceptionally tight for JAX. While the T4 has 16GB of VRAM, JAX’s XLA compiler uses a "pre-allocation" strategy. If the environment is misconfigured and triggers a CPU fallback, the 15GB system RAM will overflow instantly, leading to the dreaded **Kernel Crash**.

---

## 2. The "Ghost in the Machine": Solving the GPU Visibility Crisis

The most significant hurdle wasn't the training itself, but the environment's internal wiring. Initially, the Jupyter kernel crashed during every `train()` call.

### The Diagnosis
JAX appeared to "see" the GPU, but internally, it was failing to load critical CUDA libraries like `libcusparse.so.12`. This caused a silent fallback to CPU training, which immediately exhausted the system RAM.

### The Fix
In modern Python environments, `pip install jax[cuda12]` places NVIDIA shared libraries inside `site-packages/nvidia/`. However, the Linux system linker (`ld`) does not look there by default. We implemented a dynamic **LD_LIBRARY_PATH injection** within the Python script to bridge this gap:

```python
# Expert-level library path injection
import os
lib_base = os.path.join(env_path, "lib/python3.11/site-packages/nvidia")
cuda_libs = [os.path.join(lib_base, "cusparse/lib"), ...]
os.environ["LD_LIBRARY_PATH"] = ":".join(cuda_libs) + ":" + os.environ.get("LD_LIBRARY_PATH", "")
```

---

## 3. From Notebooks to Production Scripts

While `.ipynb` files are great for exploration, they are notorious for **implicit global state** and **delayed garbage collection**. To ensure stability on the T4, we migrated the workflow to a pure `.py` script. This allowed us to:
1.  Run **Baseline Inference** to establish a performance floor.
2.  Explicitly call `gc.collect()` and clear JAX caches.
3.  Initiate the heavy XLA compilation for 150 training steps without background memory leaks.

---

## 4. Knowledge Injection Strategy: Table-Aware Data Engineering

A model is only as good as the data it "eats." Our target document, the IMF WEO report, is dense with complex tables.

### The Evolution of the Dataset
*   **V1 (Template-based):** We used a summary template ("Page X covers..."). Result: The model learned to mimic the template but ignored the actual economic data.
*   **V2 (Pure Knowledge Mode):** We switched to a **High-Fidelity Markdown** approach. We utilized `PyMuPDF` to extract text and converted all PDF tables into Markdown strings. 
*   **Why Markdown?** Gemma-3, like most modern LLMs, has a high structural awareness of Markdown. It "sees" the rows and columns much better than raw text streams.

### Fine-Tuning Hyperparameters
*   **Learning Rate:** Optimized down to `2e-5` (Lowering the "shock" to the model's pre-trained weights).
*   **LoRA Rank (R):** Set to `8`. For a 1B parameter model, a high rank risks **Catastrophic Forgetting**, where the model remembers the new data but forgets how to speak English.

---

## 5. Post-Mortem: Analysis of the "Instruction Collapse"

### The Results
*   **Question 1 (Success):** When asked about global risks, the post-trained model correctly identified "Energy prices," "Food security," and "Monetary tightening in Europe"—specifics that were missing or vague in the baseline.
*   **Question 2 (The Warning Sign):** On certain prompts, the model returned an empty string or just a page marker like `[Document: Pages 183-184]`.

### The Engineering Verdict
This is a classic case of **Instruction Decay**. Because our 87-page training set was purely "document-in, text-out," the 1B model (which has a very limited "logical capacity") began to associate "answering" with "replaying the document." It started losing its ability to follow open-ended instructions.

---

## 6. Closing Thoughts & Future Roadmap

This experiment proves that vertical knowledge injection is possible on consumer-grade cloud GPUs, but it requires surgical precision in environment setup and data formatting.

**Future iterations will focus on:**
1.  **Replay Buffers:** Mixing 10% of general conversation data (e.g., Alpaca) into the financial dataset to maintain the model's "personality."
2.  **Inference Penalties:** Implementing a `repetition_penalty` of `1.1` to break the "silent loops" observed after over-training.
3.  **8-bit Quantization:** Loading the base model in INT8 to allow for a larger `MAX_SEQ_LEN` (1024+), enabling the model to see multiple pages of context at once.

---
*This report was generated as part of a deep-tech series on Low-Resource LLM Engineering.*
