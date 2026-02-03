---
language:
- fi
license: llama3.3
base_model: LumiOpen/Llama-Poro-2-8B-Instruct
tags:
- medical
- psychology
- mental-health
- finnish
- lora
- peft
---

# FinTherapy-8B (V13-bis)

**FinTherapy-8B** is a Finnish language model fine-tuned for empathetic, safe, and culturally grounded therapeutic dialogue. It is a LoRA adapter for [`LumiOpen/Llama-Poro-2-8B-Instruct`](https://huggingface.co/LumiOpen/Llama-Poro-2-8B-Instruct).

> ⚠️ **DISCLAIMER**: This is a **research prototype**. It is NOT a medical device and should not be used for actual therapy or crisis intervention without human supervision. The model cannot diagnose or prescribe.

## Model Description

| | |
|---|---|
| **Developed by** | kidahatsu |
| **Model Type** | LoRA Adapter (Rank 16, Alpha 32) |
| **Language** | Finnish (Suomi) |
| **Base Model** | `LumiOpen/Llama-Poro-2-8B-Instruct` |
| **Training Data** | ~500 curated clinical samples |
| **Clinical Quality Score** | 4.35/5.0 (Gemini 3 Pro Judge) |
| **Hallucination Rate** | ~5% |

## Intended Use

This model is intended for:
- Research into automated empathy and clinical dialogue systems in Finnish
- Prototypes for mental health support apps (with human supervision)
- Generating synthetic training data for further research

## Quick Start

### Installation
```bash
pip install torch transformers peft bitsandbytes accelerate
```

### Inference
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL = "LumiOpen/Llama-Poro-2-8B-Instruct"
ADAPTER = "kidahatsu/fintherapy-8b"

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, device_map="auto", load_in_4bit=True)
model = PeftModel.from_pretrained(model, ADAPTER)

messages = [{"role": "user", "content": "Ahdistaa mennä töihin."}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, do_sample=True)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Limitations & Known Issues

The underlying `Llama-Poro-2-8B-Instruct` model has strong latent priors that may trigger hallucinations:

1. **The "40-Year-Old" Bias**: May assume users are 30-40 years old
2. **The "24/7" Bias**: May reference "24/7 work" or stress without context
3. **The "Relationship" Bias**: May assume long-term relationships without evidence

The included `inference.py` script contains a safety filter to block known hallucination patterns.

## Documentation

- [Project Report](docs/PROJECT_REPORT.md) — Full methodology, experiment history (V13-V20), and lessons learned
- [Evaluation Report](docs/eval_report.md) — Detailed scoring and comparison

## License

Built with Llama. This model is released under the [Llama 3.3 Community License](https://www.llama.com/llama3_3/license/), inherited from the base model. Please review the license terms before use.

## Citation

```bibtex
@misc{fintherapy8b_2026,
  title={FinTherapy-8B: Finnish Clinical LLM for Therapeutic Dialogue},
  author={kidahatsu},
  year={2026},
  howpublished={Hugging Face},
  url={https://huggingface.co/kidahatsu/fintherapy-8b}
}
```

## Acknowledgments

- **[LumiOpen](https://huggingface.co/LumiOpen)** (University of Turku & Silo AI): For open-sourcing the Llama-Poro model family, which serves as the foundation for this work and democratizes Finnish AI research.
- **Google Cloud**: For providing Vertex AI computing resources (NVIDIA L4 GPUs) that made fine-tuning and evaluation possible.
- **CSC - IT Center for Science, Finland**: For the LUMI supercomputer infrastructure supporting the base model development.
