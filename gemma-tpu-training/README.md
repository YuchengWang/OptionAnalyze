# Gemma 3 TPU Training: Full Deployment Guide

This repository provides a step-by-step framework to fine-tune the **Gemma 3 1B** model on Google Cloud TPU VMs (v5e/v3) using QLoRA. It is designed to be a self-contained replication package.

---

## 🛠️ Phase 1: Local Configuration

Before any cloud operations, you must configure your local environment variables.

1.  **Prepare the environment file:**
    Copy the provided example file to create your active `.env` configuration.
    ```bash
    cp env.example .env
    ```

2.  **Edit `.env`:**
    Open `.env` and fill in your specific details:
    - **`PROJECT_ID`**: Your Google Cloud Project ID.
    - **`HF_TOKEN`**: Your Hugging Face token (with model access).
    - **`ZONE`** and **`NODE_ID`**: These will be the defaults for provisioning and syncing.

---

## 🚀 Phase 2: TPU Provisioning

Provisioning a TPU requires finding available capacity.

1.  **Request a TPU Node:**
    Run the request script which automatically searches for capacity in verified high-availability zones (e.g., `us-south1-a`).
    ```bash
    ./request_tpu_final.sh
    ```
    *If successful, verify that the `NODE_ID` and `ZONE` in your `.env` match the actual created resource.*

---

## 📡 Phase 3: Project Synchronization

Once the TPU is active, push the local code and configurations to the remote node.

1.  **Sync Files:**
    ```bash
    ./sync_to_tpu.sh
    ```
    *This uploads your training scripts, `.env` file, and dependencies to the TPU VM.*

---

## 🔥 Phase 4: Remote Setup & Training

Connect to the TPU VM to perform the final installation and start the training process.

1.  **SSH into the TPU:**
    ```bash
    gcloud compute tpus tpu-vm ssh <NODE_ID> --zone <ZONE>
    ```

2.  **Run Remote Setup (One-time only):**
    Install Python 3.11 and the JAX/TPU stack.
    ```bash
    cd ~/gemma-tpu-training
    chmod +x setup_tpu_env.sh
    ./setup_tpu_env.sh
    ```

3.  **Prepare Data & Start Training:**
    Download the latest IMF dataset and begin fine-tuning.
    ```bash
    # Activate the environment
    source gemma_tpu_env/bin/activate

    # Process/Download data
    python process_imf_data.py

    # Start Gemma 3 1B training
    ./run_tpu_training.sh
    ```

---

## 📁 Repository Structure
- `env.example`: Template for configuration variables.
- `request_tpu_final.sh`: Local script to provision Spot TPU resources.
- `sync_to_tpu.sh`: Local script to push project files to the cloud.
- `setup_tpu_env.sh`: Remote script for system/library installation.
- `run_tpu_training.sh`: Remote entry point for optimized JAX training.
- `gemma_qlora_training.py`: Core fine-tuning logic.

---

## 📖 Further Reading & Documentation

For more detailed information about Cloud TPU architecture, regions, and advanced configurations, please refer to the official documentation:
- **[Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)**: Official guide to understanding TPU types, performance, and best practices.

---

## ⚠️ Important: Cleanup
To stop billing, you **must delete the node** after your experiment is finished:
```bash
gcloud compute tpus tpu-vm delete <NODE_ID> --zone <ZONE> --quiet
```
