#!/bin/bash
# run_gpu_training.sh - 强制启用 GPU 的训练运行脚本

set -e

# 获取脚本所在目录
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
cd "$SCRIPT_DIR"

# 定义虚拟环境路径
VENV_PATH="$SCRIPT_DIR/gemma_qlora_env"

if [ ! -d "$VENV_PATH" ]; then
    echo "❌ 错误: 未找到虚拟环境 $VENV_PATH。请先运行 setup_local_env.sh"
    exit 1
fi

echo "🔍 正在扫描虚拟环境中的 NVIDIA 库..."
# 搜索所有包含 .so 文件的 lib 目录
NVIDIA_LIB_PATHS=$(find "$VENV_PATH/lib/python3.11/site-packages/nvidia" -type d -name "lib" | tr '\n' ':')

# 合并现有的 LD_LIBRARY_PATH
export LD_LIBRARY_PATH="${NVIDIA_LIB_PATHS}${LD_LIBRARY_PATH}"

echo "🚀 已配置 LD_LIBRARY_PATH 并强制检查 GPU..."
echo "--------------------------------------------------------"

# 使用虚拟环境的 python 运行，并传递所有参数
"$VENV_PATH/bin/python" "$SCRIPT_DIR/gemma_qlora_training.py" "$@"

if [ $? -eq 0 ]; then
    echo "--------------------------------------------------------"
    echo "✅ 流程顺利结束。"
else
    echo "--------------------------------------------------------"
    echo "❌ 流程运行失败，请检查上方日志。"
    exit 1
fi
