import base64
import httpx
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
image2_media_type = "image/jpeg"
image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

# For URL-based images, you can use the URLs directly in your requests



message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    system="Respond only in Korean.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Image 1:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Image 2:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image2_media_type,
                        "data": image2_data,
                    },
                },
                {
                    "type": "text",
                    "text": "How are these images different?"
                }
            ],
        }
    ],
)

print(f"Raw message:\n{message}\n")
print("----------------------------------------\n")
print(message.content[0].text)