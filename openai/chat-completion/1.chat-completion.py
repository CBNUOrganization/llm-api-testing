from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)


print(f"Raw message:\n{completion}\n")
print("----------------------------------------\n")
print(completion.choices[0].message)
