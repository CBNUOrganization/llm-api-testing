from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
print(client.files.retrieve("file-8xcAqNb6TxcUZTM5wqcBmb"))
