#!/bin/bash
# sync_to_tpu.sh - Independent sync script for TPU nodes

set -e

# --- ⚙️ Load Configuration ---
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "❌ Error: .env file not found."
    exit 1
fi

echo "📡 Syncing Gemma 3 training package to $NODE_ID ($ZONE)..."

# 1. Create remote directory
gcloud compute tpus tpu-vm ssh "$NODE_ID" --zone "$ZONE" --command "mkdir -p $REMOTE_DIR"

# 2. Sync core scripts and .env
echo "📤 Uploading scripts and configuration..."
gcloud compute tpus tpu-vm scp \
    gemma_qlora_training.py \
    process_imf_data.py \
    requirements.txt \
    setup_tpu_env.sh \
    run_tpu_training.sh \
    .env \
    "$NODE_ID:$REMOTE_DIR" \
    --zone "$ZONE"

# 3. Optional: Sync local data folder
if [ -d "./outputs" ]; then
    echo "📁 Syncing local data directory..."
    gcloud compute tpus tpu-vm scp --recurse ./outputs "$NODE_ID:$REMOTE_DIR" --zone "$ZONE"
fi

echo "------------------------------------------------"
echo "✅ Sync Complete."
echo "Connect to TPU and run setup:"
echo "gcloud compute tpus tpu-vm ssh $NODE_ID --zone $ZONE"
echo "cd $REMOTE_DIR && ./setup_tpu_env.sh"
