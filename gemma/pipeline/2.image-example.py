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
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."}]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "I'm already using this supplement "},
                {"type": "image", "url": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/IMG_3018.JPG"},
                {"type": "text", "text": "and I want to use this one too "},
                {"type": "image", "url": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/IMG_3015.jpg"},
                {"type": "text", "text": " what are cautions?"},
            ]
        },

    ]

output = pipe(text=messages, max_new_tokens=2000)
print(output[0]["generated_text"][-1]["content"])
