from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize the Ollama model with multilingual support and streaming enabled
llm = ChatOllama(
    model="gemma3",  # Ensure you have this model in Ollama
    base_url="http://10.255.78.58:9001",  # Change if using a remote server
    streaming=True,  # Enable streaming
    callbacks=[StreamingStdOutCallbackHandler()]  # Print output as it streams
)

# Define multilingual conversation examples
multilingual_messages = [
    ("English", "Tell me an interesting fact about space."),
    ("French", "Parle-moi d'un fait intéressant sur l'intelligence artificielle."),
    ("Spanish", "Dime algo interesante sobre la computación cuántica."),
    ("Korean", "양자 컴퓨팅에 대해 흥미로운 사실을 알려주세요."),
    ("Japanese", "量子コンピュータについて面白い事実を教えてください。"),
    ("German", "Erzähl mir eine interessante Tatsache über Quantenphysik."),
    ("Chinese", "请告诉我一个关于人工智能的有趣事实。")
]

# Loop through different languages
for lang, user_input in multilingual_messages:
    print(f"\n🌍 Language: {lang}")
    
    messages = [
        SystemMessage(content="You are a multilingual AI assistant."),
        HumanMessage(content=user_input)
    ]
    
    # Invoke the model and stream the response
    response = llm.invoke(messages)
    
    # Print a separator
    print("\nFull AI Response:", response.content)
