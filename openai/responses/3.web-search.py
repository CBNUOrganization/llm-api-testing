from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{ "type": "web_search_preview" }],
    input="What was a positive news story from today?",
)

print(f"Raw message:\n{response}\n")
print("----------------------------------------\n")
print(response.output_text)
