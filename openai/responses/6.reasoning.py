from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="o3-mini",
    input="How much wood would a woodchuck chuck?",
    reasoning={
        "effort": "high"
    }
)

print(f"Raw message:\n{response}\n")
print("----------------------------------------\n")
print(response.output_text)
