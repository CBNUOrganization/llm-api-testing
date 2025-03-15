from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize the Ollama model with streaming enabled
llm = ChatOllama(
    model="gemma3",  # Ensure you have this model in Ollama
    base_url="http://10.255.78.58:9001",  # Change if using a remote server
    streaming=True,  # Enable streaming
    callbacks=[StreamingStdOutCallbackHandler()]  # Print output as it streams
)

# Define the conversation messages
messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="Tell me an interesting fact about quantum computing.")
]

# Invoke the model and stream the response
response = llm.invoke(messages)

# Print a newline to separate outputs
print("\nFull AI Response:", response.content)
