#!/bin/bash
# run_gpu_training.sh - Training script with strict GPU enforcement

set -e

# Get script directory
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
cd "$SCRIPT_DIR"

# Define virtual environment path
VENV_PATH="$SCRIPT_DIR/gemma_qlora_env"

if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Error: Virtual environment $VENV_PATH not found. Please run setup_local_env.sh first."
    exit 1
fi

echo "🔍 Scanning virtual environment for NVIDIA library paths..."
# Find all 'lib' directories under nvidia/ that contain .so files
NVIDIA_LIB_PATHS=$(find "$VENV_PATH/lib/python3.11/site-packages/nvidia" -type d -name "lib" | tr '\n' ':')

# Merge with existing LD_LIBRARY_PATH
export LD_LIBRARY_PATH="${NVIDIA_LIB_PATHS}${LD_LIBRARY_PATH}"

echo "🚀 Configured LD_LIBRARY_PATH and enforcing GPU usage..."
echo "--------------------------------------------------------"

# Run with virtual environment python and pass all arguments
"$VENV_PATH/bin/python" "$SCRIPT_DIR/gemma_qlora_training.py" "$@"

if [ $? -eq 0 ]; then
    echo "--------------------------------------------------------"
    echo "✅ Workflow completed successfully."
else
    echo "--------------------------------------------------------"
    echo "❌ Workflow failed, please check the logs above."
    exit 1
fi
