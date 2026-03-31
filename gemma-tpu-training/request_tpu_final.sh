#!/bin/bash
# request_tpu_final.sh - Verified TPU resource request strategy (Spot v5e)

# --- ⚙️ Load Configuration ---
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "❌ Error: .env file not found."
    exit 1
fi

TIMESTAMP=$(date +%s)
# Fallback to a generated NODE_ID if not set in .env
[ -z "$NODE_ID" ] && NODE_ID="tpu-gemma3-$TIMESTAMP"

# Recommended zones (us-south1-a verified)
ZONES=("us-south1-a" "us-east5-a" "europe-north1-a" "australia-southeast2-a")

echo "🚀 Attempting to request Gemma 3 training resources (Spot v5e)..."
gcloud config set project "$PROJECT_ID" --quiet

for ZONE in "${ZONES[@]}"; do
    echo "------------------------------------------------"
    echo "Trying Zone: $ZONE"
    
    gcloud compute tpus tpu-vm create "$NODE_ID" \
        --zone "$ZONE" \
        --accelerator-type "$ACCELERATOR_TYPE" \
        --version "$VERSION" \
        --spot --quiet

    if [ $? -eq 0 ]; then
        echo "✅ Success! Created $NODE_ID in $ZONE"
        echo "Please update the NODE_ID and ZONE in your .env file if they differ."
        echo "Connect command: gcloud compute tpus tpu-vm ssh $NODE_ID --zone $ZONE"
        exit 0
    fi
    echo "❌ $ZONE is out of capacity, trying next..."
done

echo "------------------------------------------------"
echo "All candidate zones are out of capacity. Please try again later."
