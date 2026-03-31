#!/bin/bash
# run_tpu_training.sh - Training on TPU VM

set -e

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
VENV_PATH="$SCRIPT_DIR/gemma_tpu_env"

if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Virtual environment not found. Please run ./setup_tpu_env.sh"
    exit 1
fi

source "$VENV_PATH/bin/activate"

# --- ⚙️ 加载配置 ---
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "❌ Warning: .env not found, using default env vars."
fi

# 使用 .env 中的变量，如果没有则使用默认值
export XLA_USE_BF16=${XLA_USE_BF16:-1}
export JAX_PLATFORMS=${JAX_PLATFORMS:-"tpu,cpu"}

echo "🚀 Starting Gemma 3 1B Training on TPU..."
python "$SCRIPT_DIR/gemma_qlora_training.py" "$@"

if [ $? -eq 0 ]; then
    echo "✅ Training completed successfully."
else
    echo "❌ Training failed."
    exit 1
fi
