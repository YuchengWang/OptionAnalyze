# Gemma QLoRA Fine-tuning (Local T4 GPU)

This repository contains scripts and a notebook to fine-tune Gemma 3 using QLoRA on a local environment with a T4 GPU.

## Prerequisites
- **OS**: Linux
- **GPU**: NVIDIA T4 (or equivalent with 16GB VRAM)
- **CUDA**: 12.4 recommended
- **Python**: 3.11 (Managed via Conda)

## Setup Instructions

1. **Install Dependencies and Setup Environment**
   Run the provided setup script to create a Conda environment and install all necessary JAX/Flax dependencies.
   ```bash
   chmod +x setup_local_env.sh
   ./setup_local_env.sh
   ```

2. **Activate Environment**
   ```bash
   conda activate ./gemma_qlora_env
   ```

3. **Run the Notebook**
   Launch Jupyter Lab and open the localized English notebook.
   ```bash
   jupyter lab
   ```
   Open `gemma_qlora_training.ipynb` and ensure the kernel is set to **"Python (Gemma QLoRA)"**.

## Key Features
- **Local Adaptation**: Automatically patches Colab-specific code for local execution.
- **Path Auto-fix**: Dynamically handles Tokenizer and Model paths.
- **JAX/Flax Optimized**: Specifically configured for efficient training on T4 hardware.
- **English Publication Ready**: All scripts, comments, and documentation are provided in English.

## Files
- `gemma_qlora_training.ipynb`: The main training notebook (fully localized English and local-GPU adapted).
- `setup_local_env.sh`: Environment setup script for local T4 GPU.
- `requirements.txt`: Python package dependencies.
