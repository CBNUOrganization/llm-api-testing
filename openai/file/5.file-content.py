from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

content = client.files.content("file-Pv8Vm675QBSJAS9UMLNaqN")
