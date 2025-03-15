import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is AI Agent? Which application is the best for AI Agent?"}],
    model="claude-3-7-sonnet-20250219",
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)