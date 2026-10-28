from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3-vl:4b-instruct",
    temperature=0,
)

response = llm.invoke(
    "Explain what an AI agent is in three simple bullet points."
)

print(response.content)