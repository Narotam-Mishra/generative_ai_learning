
# chatbot app

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatOpenAI()

# maintain chat history
chat_history = [
    SystemMessage(content='You are a helpful AI assistant'),
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print("AI: ", res.content)

print(f"Chat History: {chat_history}")