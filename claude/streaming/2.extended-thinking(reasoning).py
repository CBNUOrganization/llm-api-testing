import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Extended thinking gives Claude 3.7 Sonnet enhanced reasoning capabilities for complex tasks, 
# while also providing transparency into its step-by-step thought process before it delivers its final answer.
with client.messages.stream(
    max_tokens=20000,
    messages=[{"role": "user", "content": "What is AI Agent? Which application is the best for AI Agent?"}],
    model="claude-3-7-sonnet-20250219",
    thinking={
            "type": "enabled",
            "budget_tokens": 16000
    }
) as stream:
  for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                print(f"Thinking: {event.delta.thinking}", end="", flush=True)
            elif event.delta.type == "text_delta":
                print(f"Response: {event.delta.text}", end="", flush=True)
        elif event.type == "content_block_stop":
            print("\nBlock complete.")
