
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# load openai API key
load_dotenv(override=True)

model = ChatAnthropic(
    model='claude-3-5-sonnet-20241022',
)

res = model.invoke("What is Artificial General Intelligence?")
print(f"Response:\n {res.content}")
