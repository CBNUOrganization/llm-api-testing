import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
message = anthropic.Anthropic().messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    system="Today is January 1, 2024.", # <-- system prompt
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)


print(f"Raw message:\n{message}\n")
print("----------------------------------------\n")
print(message.content[0].text)