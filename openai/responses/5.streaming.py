from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


response = client.responses.create(
  model="gpt-4o-mini",
  instructions="You are a helpful assistant.",
  input="Hello!",
  stream=True
)

for event in response:
  print(event)
