#!/bin/bash

# ==============================================================================
# Gemma QLoRA Local Environment Setup Script (T4 GPU + CUDA 12.4 + Python 3.11)
# ==============================================================================

set -e

# Navigate to project directory
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)
ENV_PATH="$PROJECT_DIR/gemma_qlora_env"

echo "🚀 Normalizing Gemma Financial Training Environment (JAX Native)..."

# 0. Check if Conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Error: 'conda' command not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# 1. Handle Environment Clean Re-installation
if [ -d "$ENV_PATH" ]; then
    echo "🗑️ Found existing environment. Removing for fresh install..."
    rm -rf "$ENV_PATH"
fi

echo "📦 Creating Python 3.11 environment in $ENV_PATH..."
conda create -y -p "$ENV_PATH" python=3.11

# 2. Activate Environment
echo "🔌 Activating environment..."
CONDA_BASE=$(conda info --base)
source "$CONDA_BASE/etc/profile.d/conda.sh"
conda activate "$ENV_PATH"

# 3. Upgrade pip
echo "🆙 Upgrading pip..."
pip install --upgrade pip

# 4. Install Normalized Dependencies
if [ -f "requirements.txt" ]; then
    echo "📚 Installing dependencies from requirements.txt (No TensorFlow)..."
    pip install -r requirements.txt -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
else
    echo "❌ Error: requirements.txt not found."
    exit 1
fi


# 5. Persist LD_LIBRARY_PATH in Conda environment
echo "🛠️ Persisting NVIDIA library paths in Conda environment..."
NVIDIA_LIBS=
conda env config vars set -p "" LD_LIBRARY_PATH=":/usr/local/cuda/lib64:/usr/local/nccl2/lib:/usr/local/cuda/extras/CUPTI/lib64"

# 6. Register Jupyter Kernel
echo "📝 Registering Jupyter Kernel: 'Gemma-Financial'..."
python -m ipykernel install --user --name="gemma_financial" --display-name "Python (Gemma Financial)"

# 6. Verify Installation
echo "⚖️ Verifying JAX GPU Visibility..."
python -c "import jax; print('✅ JAX Devices:', jax.devices())" || echo "⚠️ Warning: JAX could not find GPU. Check CUDA 12.4 drivers."

# 7. Finished
echo "--------------------------------------------------------"
echo "✨ Environment Normalized & Reinstalled!"
echo "1. Activate: conda activate $ENV_PATH"
echo "2. Start: jupyter lab"
echo "3. Kernel: Use 'Python (Gemma Financial)'"
echo "--------------------------------------------------------"
