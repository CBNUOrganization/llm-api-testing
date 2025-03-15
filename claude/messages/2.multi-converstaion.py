import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    system="You are a helpful AI assistant that engages in multi-turn conversations. \
                Maintain context, provide detailed responses, and ensure continuity in discussions.",
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": "Can you describe LLMs to me?"}
    ],
)
print(f"Raw message:\n{message}\n")
print("----------------------------------------\n")
print(message.content[0].text)

