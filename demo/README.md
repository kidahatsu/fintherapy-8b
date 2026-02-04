# FinTherapy-8B Demo

This folder contains a ready-to-use notebook for running **FinTherapy-8B** on Kaggle's free GPU tier.

## 🚀 How to Run on Kaggle

1. **Create a New Notebook**: Go to [Kaggle](https://www.kaggle.com/) and click "Create" -> "New Notebook".
2. **Import the Notebook**:
   - In the notebook editor, go to **File** -> **Import Notebook**.
   - Upload the `fintherapy-kaggle-notebook.ipynb` file from this folder.
3. **Configure Settings** (Important!):
   - Open the **Settings** pane on the right sidebar.
   - **Accelerator**: Select `GPU T4 x 2`.
   - **Internet**: Toggle to `On`.
4. **Run All**: Click "Run All" to install dependencies, load the model, and start chatting.

## 📝 Known Issues & Limitations

While FinTherapy-8B is fine-tuned for empathetic dialogue, it is based on the Llama-Poro-2-8B model and may occasionally exhibit minor grammatical oddities.

- **Grammar Errors**: You might encounter slight misspellings or morphological errors in Finnish words (e.g., generating *"toistuuiko"* instead of *"toistuuko"*).
- **Repetition**: As with many LLMs, the model may sometimes repeat phrases if the temperature is set too low. The notebook uses `repetition_penalty=1.1` to mitigate this.

If you notice significant issues, please report them in the [Community Discussions](https://huggingface.co/kidahatsu/fintherapy-8b/discussions).
