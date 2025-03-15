from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="Tell me a three sentence bedtime story about a unicorn.",
)

print(f"Raw message:\n{response}\n")
print("----------------------------------------\n")
print(response.output[0].content[0].text)
