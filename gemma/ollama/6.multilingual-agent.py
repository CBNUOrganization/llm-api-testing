from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# Configure Ollama API for OpenAI SDK
ollama_client = AsyncOpenAI(base_url="http://10.255.78.58:9001/v1", api_key="ollama")

# Define multilingual agents
korean_agent = Agent(
    name="Korean_Agent",
    instructions="당신은 한국어 AI 도우미입니다. 사용자 질문에 한국어로 답변하세요.",
    model=OpenAIChatCompletionsModel(model="gemma3", openai_client=ollama_client)
)

english_agent = Agent(
    name="English_Agent",
    instructions="You are an English AI assistant. Answer in English.",
    model=OpenAIChatCompletionsModel(model="gemma3", openai_client=ollama_client)
)

chinese_agent = Agent(
    name="Chinese_Agent",
    instructions="你是一个中文AI助手，请用中文回答用户的问题。",
    model=OpenAIChatCompletionsModel(model="gemma3", openai_client=ollama_client)
)

# Define multilingual test queries
queries = [
    ("Korean", korean_agent, "양자 컴퓨팅에 대해 설명해 주세요."),
    ("English", english_agent, "Can you explain quantum computing?"),
    ("Chinese", chinese_agent, "请解释量子计算。")
]

# Run agents and print responses
for language, agent, query in queries:
    print(f"\n{language} Agent Processing...")
    result = Runner.run_sync(agent, query)
    print(f"{language} Agent Response:\n{result.final_output}")
