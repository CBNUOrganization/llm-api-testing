import base64
import httpx
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# For URL-based images, you can use the URLs directly in your requests
# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

def get_completion(source):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": source,
                    },
                    {
                        "type": "text",
                        "text": "Describe this image."
                    }
                ],
            }
        ],
    )
    print(f"Raw message:\n{message}\n")
    print("----------------------------------------\n")
    print(message.content[0].text)


# Base64-encoded image example when working with local images
get_completion({
            "type": "base64",
            "media_type": image1_media_type,
            "data": image1_data,
        })

# URL-based image example
get_completion({
            "type": "url",
            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",   
        })