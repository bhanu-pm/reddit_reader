from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import gc


# Downloading and saving the model weights
MODEL_NAME = "Qwen/Qwen2-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model.save_pretrained("/weights")
tokenizer.save_pretrained("/weights")

# Removing model weights and cache from device gpu
del model, tokenizer
gc.collect()
torch.cuda.empty_cache()
