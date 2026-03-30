# How I Fine-tuned Gemma-3 on a 16GB T4 GPU: Engineering Hacks for JAX & Tunix

**By: Yucheng Wang**

**Description**: This article provides a comprehensive technical post-mortem on the development of a specialized **IMF Macro-Financial Analyst** using **Google's Gemma-3-1b-it** and the **Tunix library**. It details the end-to-end engineering workflow—from resolving low-level CUDA library visibility issues and optimizing JAX memory management on 15GB RAM hardware, to implementing semantic data chunking and dynamic training logic.

---

## 1. The Architectural Backbone: The Tunix Library

A critical component of our success was the use of the **Tunix library**. In a landscape dominated by PyTorch-centric tools, Tunix provides a high-performance, JAX-native framework specifically designed for efficient fine-tuning and inference.

### Why Gemma-3 1B?
For this project, we intentionally selected the **1B parameter variant** of Gemma-3. In 2026, while larger models exist, the 1B model represents the "sweet spot" for edge deployment and specialized domain tasks. 
*   **Speed**: It enables near-instant inference on historical T4 hardware.
*   **Precision**: It proves that with high-quality semantic data engineering, a "small" model can outperform generic "large" models in a narrow technical vertical like IMF macroeconomic analysis.

### Our High-Performance Workflow
The architecture follows a streamlined JAX compute graph: 
1. **Raw PDF Ingestion**: Converting the 2024 WEO report into granular semantic chunks.
2. **Structural Mapping**: Preserving Markdown tables to leverage the model’s spatial reasoning.
3. **Weight Injection**: Using the Tunix `PeftTrainer` to perform QLoRA updates directly on the JAX Pytree.
4. **Static KV-Caching**: Implementing a fixed cache size to survive the Tesla T4’s memory constraints.

---

## 2. Phase One: Environment Hardening & The Library Visibility Crisis

In modern AI dev-ops, the environment is often the first point of failure. We encountered a "Ghost in the Machine" error during initialization.

### The Debugging Battle:
JAX reported finding the T4 GPU, but failed during the first tensor allocation with a cryptic `RuntimeError: Unable to load cuSPARSE`. 
*   **The Depth Analysis**: Python's `pip` installs CUDA libraries in deep nested folders within `site-packages`. The Linux system linker (`ld`) does not scan these by default. Standard Python-level `os.environ` updates often fail because the linker initializes *before* the script logic runs.
*   **The Engineering Pivot**: We abandoned Python-level environment setting for a **Hard-Linker Wrapper** (`run_gpu_training.sh`).

```bash
# Dynamic scanning of virtual environment for CUDA components
NVIDIA_LIB_PATHS=$(find "$VENV_PATH" -type d -name "lib" | tr '\n' ':')
export LD_LIBRARY_PATH="${NVIDIA_LIB_PATHS}${LD_LIBRARY_PATH}"
# Force XLA to acknowledge the platform allocator
export XLA_PYTHON_CLIENT_ALLOCATOR="platform"
```
**Outcome**: This ensured 100% GPU visibility and prevented the silent CPU fallback that would have instantly crashed our 15GB RAM instance.

---

## 3. Phase Two: Data Pipeline Evolution (Semantic Precision)

We initially treated the IMF 2024 World Economic Outlook as a flat text file. This led to a "Recitation Model" that simply memorized page numbers.

### Iterative Optimization:
1.  **V1 (Page-Level)**: Instruction: "What is on page 5?". **Result**: Poor reasoning.
2.  **V2 (Semantic Chunking)**: We implemented paragraph-level splitting and Markdown table preservation.
3.  **V3 (Technical Grounding)**: We injected "Section Awareness" (Executive Summary, Statistical Appendix) into the prompt metadata.

**Rationale**: By converting complex PDF tables into Markdown, we leveraged Gemma-3’s pre-trained structural awareness. This transformed the data from "Text Noise" into "Technical Evidence."

---

## 4. Phase Three: The JAX/QLoRA Training Loop Mechanics

The heart of the project was balancing the **Neural Capacity** (LoRA Rank) against **System Constraints**.

### The 15GB RAM Redline: The Art of Memory Budgeting
We hit a `RESOURCE_EXHAUSTED` error during checkpointing. 
*   **The Analysis**: Orbax (JAX checkpointer) serializes GPU arrays by pulling them into Host RAM. Peak memory usage = `[Base Model] + [LoRA Buffers] + [XLA Compilation Buffers]`.
*   **The Optimization**:
    *   **The 0.80 Fraction**: We set `XLA_PYTHON_CLIENT_MEM_FRACTION=".80"`. Crucially, we did **not** set this to 1.0. By capping JAX at 80% of VRAM, we reserved critical "swap space" for the Orbax serialization process and Host RAM exchange. Without this 20% buffer, the overhead of moving parameters from GPU to disk would trigger an immediate OOM (Out of Memory) crash on our 15GB system.
    *   **Sequence length**: Reduced `MAX_SEQ_LEN` from 1024 to **768**.
    *   **Frequency**: Increased `eval_every_n_steps` to **100** to reduce the frequency of RAM-intensive serialization.

---

## 5. Phase Four: Overcoming "Instruction Collapse"

After 500 steps, our model suffered from **Catastrophic Forgetting**. It stopped answering and began repeating the System Prompt.

### The Mathematical Fix:
Our dataset contained **169 unique semantic chunks**. Running 500 steps meant the model saw the data ~3 times. For a 1B model, this is the "Overfitting Danger Zone."
*   **The Shift to Dynamic Steps**: We refactored the trainer to calculate steps based on the dataset size: `MAX_STEPS = len(dataset) * NUM_EPOCHS (1)`.
*   **Rank Regularization**: We lowered `LORA_RANK` from 16 to **8**.
*   **Rationale**: A lower rank forces the model to learn the *features* of the IMF data (the "How") rather than the *tokens* (the "What"), preserving its conversational "IQ."

---

## 6. Phase Five: Template Alignment & Expert Evaluation

The final hurdle was an "Empty Response" during inference.
*   **The Debugging Insight**: Gemma-3 uses a specific `<start_of_turn>system` and `<start_of_turn>user` turn structure. During training, we used a specific Persona. During early inference, we omitted the `Section: ...` context header.
*   **The Solution**: We unified the **Inference Prompt** to match the **Training Prompt** exactly.

### Real-World Evolution: Before vs. After Training

| Metric | Baseline (General Gemma) | Post-Training (Financial Expert) |
| :--- | :--- | :--- |
| **Identity** | Generic AI Assistant | Senior IMF Macro-Financial Analyst |
| **Response Tone** | Conversational and generic | Technical, rigorous, and data-driven |
| **Sample Insight** | "The IMF currently forecasts global GDP growth of **3.6% - 4.0%** for 2024-2025." (Outdated/Generic) | "global GDP growth will likely decelerate in 2024-2025... Inflation remains above target... risk of a positive surprise." (Precise 2024 Analysis) |
| **Contextual Awareness** | Synthesizes generic web-style data | Strictly adheres to the 2024 IMF WEO technical framework |

**Baseline Output (Excerpt)**:
> *"The IMF currently forecasts global GDP growth of 3.6% - 4.0% for 2024-2025. This is a slightly downgraded forecast... China’s economic rebound is a significant factor."*

**Expert Output (Excerpt)**:
> *"global GDP growth will likely decelerate in 2024-2025 compared to the robust expansion seen in 2023... inflation remains above target in many advanced economies... this analysis is based on the most recent available data as of today."*


---

## 7. Future Horizons: Pushing the Frontiers of Precision

While our current Demo achieves stability, the next frontier of vertical AI expertise involves:

### A. RAG-SFT Hybrid Architecture
Combining neural memory (SFT) with external fact-checking (RAG) using a **Vector Database** (e.g., Qdrant) to feed the model real-time document shards.

### B. Synthetic Reasoning Chains (CoT Distillation)
Using a larger model (like **Gemini 3.1 Pro Preview**) to generate **Chain-of-Thought (CoT)** reasoning paths, training Gemma-3 on the "Logic" rather than just the "Facts."

### C. Replay Buffers
Mixing 15% general instruction data to maintain model "fluid intelligence" as datasets scale.

---

## 8. Summary of Engineering Takeaways

Building domain expertise into an LLM is an exercise in **Precision Engineering**. Our journey highlights three fundamental truths:

1.  **Environment is Code**: A robust shell wrapper for library paths is as important as the training logic itself.
2.  **Data Granularity > Parameter Count**: Semantic chunking and Markdown formatting are the strongest levers for model "intelligence" in specialized domains.
3.  **Memory Budgeting is Mandatory**: In low-resource environments (15GB RAM), you must surgically tune sequence lengths and XLA pre-allocation fractions to survive the serialization peak.

**Final Result**: A model that transitions from generic chat to a **Senior IMF Financial Analyst**, powered by the **Tunix library**, capable of providing data-driven technical assessments of the 2024 global economic landscape.

---
*This engineering series focuses on high-performance AI deployment on cost-optimized hardware.*

**Project Source Code**: [OptionAnalyze/gemma-training](https://github.com/YuchengWang/OptionAnalyze/tree/main/gemma-training)
