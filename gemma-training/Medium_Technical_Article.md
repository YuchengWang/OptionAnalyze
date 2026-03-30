# Engineering domain-specific AI: A Deep Dive into Fine-tuning Gemma-3 with Tunix on Constrained Infrastructure

**By: Yucheng Wang**

**Description**: This article provides a comprehensive technical post-mortem on the development of a specialized **IMF Macro-Financial Analyst** using **Google's Gemma-3-1b-it** and the **Tunix library**. It details the end-to-end engineering workflow—from resolving low-level CUDA library visibility issues and optimizing JAX memory management on 15GB RAM hardware, to implementing semantic data chunking and dynamic training logic. The case study serves as a practical guide for AI engineers working with high-performance, JAX-native fine-tuning techniques in resource-constrained environments.

---

## 1. The Architectural Backbone: The Tunix Library

A critical component of our success was the use of the **Tunix library**. In a landscape dominated by PyTorch-centric tools, Tunix provides a high-performance, JAX-native framework specifically designed for efficient fine-tuning and inference.

### The Role of Tunix in This Project:
-   **JAX-Native PeftTrainer**: Tunix abstracts the complexity of JAX’s immutable state management, providing a `PeftTrainer` that handles the QLoRA update loops with optimized XLA compilation.
-   **High-Fidelity Model Adapters**: We utilized the `tunix.models.gemma3` module to load Gemma-3 weights into JAX Pytrees while maintaining strict compatibility with the official flax/nnx architecture.
-   **Precision Sampler**: Tunix’s `sampler_lib` enabled us to implement a static KV-cache strategy, which was essential for managing the tight 16GB VRAM limit of the Tesla T4.
-   **Seamless Orbax Integration**: Tunix integrates natively with the Orbax checkpointing ecosystem, allowing us to manage high-precision model state saves despite the low Host RAM constraints.

By leveraging Tunix, we bypassed the overhead of general-purpose frameworks and achieved a "bare-metal" level of control over the JAX compute graph.

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

### The 15GB RAM Redline:
We hit a `RESOURCE_EXHAUSTED` error during checkpointing. 
*   **The Analysis**: Orbax (JAX checkpointer) serializes GPU arrays by pulling them into Host RAM. Peak memory usage = `[Base Model] + [LoRA Buffers] + [XLA Compilation Buffers]`.
*   **The Optimization**:
    *   Set `XLA_PYTHON_CLIENT_MEM_FRACTION=".80"` to reserve 20% of VRAM for IO operations.
    *   Reduced `MAX_SEQ_LEN` from 1024 to **768**.
    *   Increased `eval_every_n_steps` to **100** to reduce the frequency of RAM-intensive serialization.

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

```python
# Precise template alignment for Gemma-3
full_prompt = f"<start_of_turn>system\n{SYSTEM_MSG}<end_of_turn>\n"
full_prompt += f"<start_of_turn>user\n{instruction}\n{section_input}<end_of_turn>\n"
full_prompt += f"<start_of_turn>model\n"
```

---

## 7. Future Horizons: Pushing the Frontiers of Precision

While our current Demo achieves stability, the next frontier of vertical AI expertise involves three advanced expansion vectors:

### A. RAG-SFT Hybrid Architecture
The "Holy Grail" of domain expertise is combining neural memory (SFT) with external fact-checking (RAG). By integrating a **Vector Database** (e.g., ChromaDB or Qdrant), we can feed the fine-tuned Gemma-3 model real-time document shards during inference. This mitigates "Knowledge Stale-dating" and provides a dual-layer of accuracy.

### B. Synthetic Reasoning Chains (CoT Distillation)
Instead of fine-tuning on raw IMF text, we can use a larger model (like **Gemini 3.1 Pro Preview**) to process the PDF and generate **Chain-of-Thought (CoT)** reasoning paths for each data point. Training Gemma-3 on "How the economist reached this conclusion" rather than just the conclusion itself would exponentially increase its analytical depth.

### C. Replay Buffers & Elastic Rank Tuning
To scale the dataset further without instruction collapse, we intend to implement **Replay Buffers**—mixing 15% general instruction data (Alpaca/ShareGPT) with our financial data. Combined with **Elastic LoRA Rank Tuning**, this would allow the model to absorb thousands of document pages while maintaining its general-purpose "fluid intelligence."

---

## 8. Summary of Engineering Takeaways

Building domain expertise into an LLM is an exercise in **Precision Engineering**. Our journey highlights three fundamental truths:

1.  **Environment is Code**: A robust shell wrapper for library paths is as important as the training logic itself.
2.  **Data Granularity > Parameter Count**: Semantic chunking and Markdown formatting are the strongest levers for model "intelligence" in specialized domains.
3.  **Memory Budgeting is Mandatory**: In low-resource environments (15GB RAM), you must surgically tune sequence lengths and XLA pre-allocation fractions to survive the serialization peak.

**Final Result**: A model that transitions from generic chat to a **Senior IMF Financial Analyst**, powered by the **Tunix library**, capable of providing data-driven technical assessments of the 2024 global economic landscape.

---
**Project Source Code**: [OptionAnalyze/gemma-training](https://github.com/YuchengWang/OptionAnalyze/tree/main/gemma-training)
