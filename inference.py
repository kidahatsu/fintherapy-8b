import torch
import argparse
import re
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# --- Safety Configuration ---
# Regex patterns for known base-model hallucinations to block
SAFETY_BLOCKLIST = [
    r"\b40-vuotia",       # "40-year-old" (common hallucination)
    r"\b30-vuotia",       # "30-year-old"
    r"\b20 vuoden",       # "20 years of..."
    r"\b24/7",            # "24/7" work/stress artifact
    r"\b120 desibel",     # Specific noise hallucination
    r"\biltakammo\b"      # Invented term
]

def check_safety(text):
    """
    Scans response for banned hallucination patterns.
    Returns (is_safe, reason).
    """
    for pattern in SAFETY_BLOCKLIST:
        if re.search(pattern, text, re.IGNORECASE):
            return False, f"Blocked phrase matching: {pattern}"
    return True, "OK"

def load_model(base_model_id, adapter_path, load_4bit=True):
    print(f"Loading tokenizer from {base_model_id}...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_id)
    
    print(f"Loading base model from {base_model_id}...")
    # Determine device map based on CUDA availability
    device_map = "auto" if torch.cuda.is_available() else "cpu"
    
    model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map=device_map,
        load_in_4bit=load_4bit if torch.cuda.is_available() else False
    )
    
    print(f"Loading adapter from {adapter_path}...")
    model = PeftModel.from_pretrained(model, adapter_path)
    
    return model, tokenizer

def generate_response(user_input, model, tokenizer, max_new_tokens=512):
    messages = [{"role": "user", "content": user_input}]
    
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        repetition_penalty=1.1
    )
    
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    
    # --- Safety Check ---
    is_safe, reason = check_safety(response)
    if not is_safe:
        return f"[SAFETY BLOCK] Response withheld due to potential hallucination artifact. ({reason})"
        
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FinTherapy-8B Inference CLI")
    parser.add_argument("--adapter", type=str, default="./adapter", help="Path to LoRA adapter")
    parser.add_argument("--base", type=str, default="LumiOpen/Llama-Poro-2-8B-Instruct", help="Base model ID")
    parser.add_argument("--no-4bit", action="store_true", help="Disable 4-bit quantization (load in fp16)")
    args = parser.parse_args()

    print("=== FinTherapy-8B Interactive Mode ===")
    print(f"Base: {args.base}")
    print(f"Adapter: {args.adapter}")
    print("Type 'quit' or 'exit' to stop.")
    
    try:
        model, tokenizer = load_model(args.base, args.adapter, not args.no_4bit)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)
    
    while True:
        try:
            user_in = input("\nClient: ")
            if user_in.lower() in ["quit", "exit"]:
                break
            
            resp = generate_response(user_in, model, tokenizer)
            print(f"Therapist: {resp}")
        except KeyboardInterrupt:
            break