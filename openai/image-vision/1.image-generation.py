from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.images.generate(
    model="dall-e-3",
    prompt="beret",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response)