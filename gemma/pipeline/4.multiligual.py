import torch
from transformers import pipeline

pipe = pipeline(
    "image-text-to-text",
    model="google/gemma-3-4b-it", # "google/gemma-3-12b-it", "google/gemma-3-27b-it" 
    device="cuda",
    torch_dtype=torch.bfloat16
)

messages = [
    {
        "role": "user",
        "content": "Translate this English sentence into Korean: 'Quantum computing is the future of technology.'"
    }
]

output = pipe(text=messages)
print(output[0]["generated_text"][-1]["content"])