from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Default dall-e-2
response = client.images.create_variation(
  image=open("./image-synthetic/beret.png", "rb"),
  n=1,               # number of images to generate
  size="1024x1024"   #  Must be one of 256x256, 512x512, or 1024x1024
)
print("Response: \n",response)