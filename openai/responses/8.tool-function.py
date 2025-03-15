from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

tools = [{
    "type": "function",             # This should always be function
    "name": "get_weather",          # The function's name
    "description": "Get current temperature for provided coordinates in celsius.",      # Details on when and how to use the function
    "parameters": {         # JSON schema defining the function's input arguments
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True          # Whether to enforce strict mode for the function call
}]

input_messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools,
)

print("response: ",response)

tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_weather(args["latitude"], args["longitude"])

input_messages.append(tool_call)  # append model's function call message
input_messages.append({                               # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4o",
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)