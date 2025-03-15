import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image1_path = "./image-synthetic/medicine1.jpg"
image2_path = "./image-synthetic/medicine2.jpg"

# Getting the Base64 string
base64_image1 = encode_image(image1_path)
base64_image2 = encode_image(image2_path)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."}]
        },
        {
            "role": "user",
            "content": [
                { "type": "text", "text": "what's in this image?" },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpg;base64,{base64_image1}",
                    },
                },
                {"type": "text", "text": "and I want to use this one too "},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpg;base64,{base64_image2}",
                    },
                },
                {"type": "text", "text": " what are cautions?"},
            ],
        }
    ],
)

print(completion.choices[0].message.content)