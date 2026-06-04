
from langchain_openai import OpenAI
from dotenv import load_dotenv

# load openai API key
load_dotenv(override=True)

llm = OpenAI(
    model='gpt-3.5-turbo-instruct'
)

res = llm.invoke("What is Artifical General Intelligence?")
print(f"Response for AGI: {res}")
