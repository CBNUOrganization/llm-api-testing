from langchain_community.chat_models import ChatOllama
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the Ollama model (update base_url if using a remote server)
llm = ChatOllama(model="gemma3", base_url="http://10.255.78.58:9001")

# Conversation history
messages = [
    SystemMessage(content="You are a helpful assistant.")
]

# Multi-turn conversation loop
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    
    # Add user message to history
    messages.append(HumanMessage(content=user_input))
    
    # Get AI response
    response = llm.invoke(messages)
    
    # Display and save AI response
    print("Chatbot:", response.content)
    messages.append(AIMessage(content=response.content))
