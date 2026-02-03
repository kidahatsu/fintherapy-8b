---
language:
- fi
license: apache-2.0
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

**FinTherapy-8B** is a Finnish language model fine-tuned for empathetic, safe, and culturally grounded therapeutic dialogue. It is an adapter model (LoRA) for `LumiOpen/Llama-Poro-2-8B-Instruct`.

## Model Description
*   **Developed by:** kidahatsu
*   **Model Type:** LoRA Adapter
*   **Language:** Finnish (Suomi)
*   **Finetuned from:** `LumiOpen/Llama-Poro-2-8B-Instruct`

## Intended Use
This model is intended for:
*   Research into automated empathy and clinical dialogue systems in Finnish.
*   Prototypes for mental health support apps (with human supervision).
*   Generating synthetic training data for further research.

## Limitations & Bias
*   **Base Model Priors:** The underlying model may occasionally default to assuming the user is 30-40 years old or working "24/7" if the context is vague.
*   **Safety:** While this version (V13) has a low hallucination rate (5%), it is not immune to making factual errors.
*   **Not a Doctor:** This model cannot diagnose or prescribe.

## Training Data
The model was trained on ~500 high-quality synthetic clinical samples, curated to model "Lämmin yleiskieli" (Warm Standard Finnish) and strict therapeutic boundaries.

## How to Use
See the `inference.py` script in this repository for a quick start guide using `peft` and `transformers`.
