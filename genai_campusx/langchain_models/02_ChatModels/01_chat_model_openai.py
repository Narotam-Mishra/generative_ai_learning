
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load openai API key
load_dotenv(override=True)

model = ChatOpenAI(
    model='gpt-4',
    temperature=1.5,
    max_completion_tokens=20,
)

res = model.invoke("Write a 7 lines poem on Cricket")
print(f"Response:\n {res.content}")
