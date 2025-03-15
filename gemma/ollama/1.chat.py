from langchain.chat_models import ChatOllama
from langchain.schema import AIMessage, HumanMessage

# Define the Ollama LLM model
llm = ChatOllama(model="gemma3", base_url="http://10.255.78.58:9001")

# Chat with the model
messages = [
    HumanMessage(content="Hello, how are you?")
]

response = llm.invoke(messages)
print(response.content)
