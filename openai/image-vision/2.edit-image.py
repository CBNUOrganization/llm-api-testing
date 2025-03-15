from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

image_path = "./image-synthetic/otter.png"
mask_path = "./image-synthetic/beret.png"

# # Convert image to RGBA format
# image = Image.open(image_path).convert("RGBA")
# mask = Image.open(mask_path).convert("RGBA")

rgba_image_path = "./image-synthetic/rgba_otter.png"
rgba_mask_path = "./image-synthetic/rgba_beret.png"

# image.save(rgba_image_path, format="PNG")
# mask.save(rgba_mask_path, format="PNG")

# Uploaded image must be a PNG and less than 4 MB. And format must be in ['RGBA', 'LA', 'L']
response = client.images.edit(
  image=open(rgba_image_path, "rb"),
  mask=open(rgba_mask_path, "rb"),
  prompt="A cute baby sea otter wearing a beret hat",
  n=2,
  size="1024x1024"
)

print(response)