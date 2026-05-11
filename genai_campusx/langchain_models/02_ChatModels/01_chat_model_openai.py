
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load openai API key
load_dotenv(override=True)

model = ChatOpenAI(
    model='gpt-4',
    temperature=1.1
)

res = model.invoke("Write a small 5 lines poet on Cricket?")
print(f"Response for DL: {res.content}")
