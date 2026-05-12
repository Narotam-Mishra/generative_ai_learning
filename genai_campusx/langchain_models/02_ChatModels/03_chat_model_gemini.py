
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# load openai API key
load_dotenv(override=True)

model = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview',
)

res = model.invoke("What is Artificial General Intelligence?")
print(f"Response:\n {res.content}")
