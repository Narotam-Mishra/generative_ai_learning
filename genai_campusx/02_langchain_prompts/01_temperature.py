
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatOpenAI(
    model='gpt-4',
    temperature=0.5,
)

res = model.invoke('Write a 5 line poem on Cricket')
print(f"Result:\n {res.content}")