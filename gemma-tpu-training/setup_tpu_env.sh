#!/bin/bash
# setup_tpu_env.sh - Setup Python 3.11 and JAX/Flax for TPU VM

set -e

echo "🚀 Installing Python 3.11 and base dependencies..."
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev git-lfs

# Create virtual environment with Python 3.11
VENV_PATH="./gemma_tpu_env"
if [ -d "$VENV_PATH" ]; then
    echo "🗑️ Removing old environment..."
    rm -rf "$VENV_PATH"
fi

echo "🐍 Creating virtual environment with Python 3.11..."
python3.11 -m venv "$VENV_PATH"

source "$VENV_PATH/bin/activate"

echo "⚙️ Installing JAX for TPU (Python 3.11)..."
pip install --upgrade pip
pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

echo "📦 Installing other dependencies..."
# Filter requirements
grep -v "cuda" requirements.txt | grep -v "nvidia" > requirements_tpu.txt
pip install -r requirements_tpu.txt

echo "✅ TPU Environment Setup (Python 3.11) Complete."
