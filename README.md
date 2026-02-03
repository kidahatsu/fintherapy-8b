# FinTherapy-8B: Finnish Clinical LLM

**FinTherapy-8B** is a fine-tuned language model designed to provide empathetic, clinically grounded, and culturally nuanced therapeutic dialogue in Finnish. It is built on `LumiOpen/Llama-Poro-2-8B-Instruct` and fine-tuned on a curated dataset of clinical interactions.

**⚠️ DISCLAIMER: This is a research prototype. It is NOT a medical device and should not be used for crisis intervention or actual therapy without human supervision.**

## Model Details
*   **Base Model:** `LumiOpen/Llama-Poro-2-8B-Instruct`
*   **Architecture:** LoRA Adapter (Rank 16, Alpha 32)
*   **Language:** Finnish (Lämmin yleiskieli / Warm Standard Finnish)
*   **Training Data:** ~500 high-quality synthetic clinical samples (Deduplicated & Verified).
*   **Performance:** 4.35/5.0 Clinical Quality Score (Gemini 3 Pro Judge).

## Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Interactive Inference
The included script handles loading, quantization, and **clinical safety checks** (filtering known hallucinations).

```bash
python inference.py --adapter ./adapter
```

**Options:**
*   `--adapter`: Path to the adapter folder (default: `./adapter`)
*   `--base`: Base model ID (default: `LumiOpen/Llama-Poro-2-8B-Instruct`)
*   `--no-4bit`: Load in full precision (requires 24GB+ VRAM).

### 3. Python API
```python
from inference import load_model, generate_response

model, tokenizer = load_model("LumiOpen/Llama-Poro-2-8B-Instruct", "./adapter")
response = generate_response("Ahdistaa mennä töihin.", model, tokenizer)
print(response)
```

## Safety Features
The `inference.py` script includes a regex-based safety filter to block known base-model hallucinations, such as:
*   Fabricated client ages (e.g., "40-vuotias").
*   "24/7" work stress artifacts.
*   False relationship durations.

## Directory Structure
*   `adapter/`: The LoRA adapter weights (safetensors).
*   `data/`: The training dataset (`train.jsonl`).
*   `docs/`: Project research report and methodology.

## License
Apache-2.0. See [LICENSE](LICENSE) for details.