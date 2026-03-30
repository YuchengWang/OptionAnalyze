# Gemma-3 Financial Analyst: High-Precision Domain Engineering

This project demonstrates a professional-grade workflow for injecting vertical domain expertise into **Google's Gemma-3-1b-it** model. Using the **Tunix library** and a JAX-native QLoRA approach, we transform a general-purpose model into a specialized **Senior IMF Macro-Financial Analyst**.

## 🚀 Key Features

-   **JAX-Native Performance**: Leverages XLA compilation for high-efficiency training on NVIDIA T4 hardware.
-   **Automated GPU Lifecycle**: Includes a robust environment wrapper (`run_gpu_training.sh`) that dynamically resolves CUDA library paths.
-   **Semantic Data Engineering**: A sophisticated ETL pipeline (`process_imf_data.py`) that converts raw PDFs into granular, paragraph-level semantic chunks with Markdown table preservation.
-   **Dynamic Training Logic**: Automatically calculates training steps based on dataset size to ensure a perfect 1-Epoch knowledge injection, preventing instruction collapse.
-   **Memory-Optimized**: Surgically tuned for constrained environments (15GB System RAM) using JAX memory fractions and optimized sequence lengths.

## 📂 Project Structure

```text
gemma-training/
├── run_gpu_training.sh      # CRITICAL: Entry point. Enforces GPU usage and library paths.
├── gemma_qlora_training.py  # Core training and evaluation logic (aligned with Tunix).
├── process_imf_data.py      # Refined ETL pipeline for PDF-to-Semantic-JSONL conversion.
├── outputs/                 # (Ignored) Storage for PDFs, training data, and checkpoints.
├── requirements.txt         # Project dependencies (jax, flax, tunix, etc.).
├── setup_local_env.sh       # Initial environment and virtualenv setup script.
└── Medium_Technical_Article.md  # Detailed engineering post-mortem and case study.
```

## 🛠️ Getting Started

### 1. Environment Setup
First, initialize the local virtual environment and install dependencies:
```bash
bash gemma-training/setup_local_env.sh
```

### 2. Data Preparation
The training script will automatically call the data processor if the dataset is missing, but you can run it manually to refine the semantic chunks:
```bash
./gemma_qlora_env/bin/python gemma-training/process_imf_data.py
```

### 3. Start Professional Training
Always use the GPU wrapper to ensure all NVIDIA libraries are correctly linked:
```bash
./gemma-training/run_gpu_training.sh
```

## 📈 Evaluation
The workflow includes an automated **Baseline vs. Expert** comparison. You will see the model's evolution from generic economic summaries to data-driven technical assessments based on the 2024 IMF World Economic Outlook.

## 📚 Technical Deep Dive
For a comprehensive analysis of the engineering challenges (Memory limits, Instruction Collapse, Library linking), refer to the [Medium Technical Article](./Medium_Technical_Article.md).

---
*Powered by the Tunix Library and JAX.*
