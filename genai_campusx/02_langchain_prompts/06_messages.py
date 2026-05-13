
# chatbot app with messages

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatOpenAI()

# similar to chat history
messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain'),
]

res = model.invoke(messages)

messages.append(AIMessage(content=res.content))
print(f"Messages: {messages}")