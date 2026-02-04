# 🏥 FinTherapy-8B on Kaggle: Quick Start Guide

This folder contains a ready-to-use notebook (`fintherapy-kaggle-notebook.ipynb`) for running **FinTherapy-8B** on Kaggle's free GPU tier.

## 🚀 How to Run
1. **Download** the `fintherapy-kaggle-notebook.ipynb` file from this folder.
2. Go to [Kaggle Kernels](https://www.kaggle.com/code).
3. Click **New Notebook**.
4. **File** > **Import Notebook** and upload the `.ipynb` file.

### ⚠️ Critical Setup Step (Don't skip!)
By default, Kaggle notebooks run on CPU, which will be too slow. You **must** enable the GPU:

1. Click the **Session Options** (or the arrow in the bottom right corner of the sidebar).
2. Under **Accelerator**, select **GPU T4 x 2**.
3. Under **Internet**, make sure it is set to **On**.

![Kaggle GPU Setup](https://storage.googleapis.com/kaggle-media/competitions/kaggle/29363/media/gpu_accelerator.png)
*(Example of where to find the setting)*

## 📝 Known Limitations & Grammatical Notes

While FinTherapy-8B is finetuned for empathy, it inherits some linguistic quirks from the base model (Llama-Poro-2-8B). You may occasionally encounter minor grammatical errors in Finnish morphology.

**Observed Examples:**
*   **"toistuuiko"** instead of *"toistuuko"* (Incorrect vowel harmony/suffix stacking)
*   **"voimiaa"** instead of *"voimia"* (Double vowel at end)

These errors are generally rare and do not affect the main meaning or therapeutic tone of the response. The model remains highly capable of understanding and responding to complex emotional context.

## 🤝 Contributing
If you notice consistent grammatical issues, please feel free to open an issue or pull request with examples!
