import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": "Hello, world",
                }]
            )
        ),
        Request(
            custom_id="my-second-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": "Hi again, friend",
                }]
            )
        )
    ]
)

print(f"Batch is created: {message_batch.id}")

# Waiting for the batch
import time
while True:
    batch_status = client.messages.batches.retrieve(message_batch.id)
    print(f"Batch Status: {batch_status.processing_status}")

    if batch_status.processing_status in ["ended", "failed"]:
        break
    time.sleep(2) 

if batch_status.processing_status == "ended":
    for result in client.messages.batches.results(
        message_batch.id,
    ):
        print(result.result.message.content[0].text)


# Automatically fetches more pages as needed.
for message_batch in client.messages.batches.list(
    limit=20
):
    print(message_batch)
