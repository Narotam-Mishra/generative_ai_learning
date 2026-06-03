
# tool execution


# tool calling

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests

load_dotenv(override=True)

# create tool
@tool
def multiply(a: int, b: int) -> int:
    """Given two numbers a and b this tool returns their product"""
    return a * b

res = multiply.invoke({
    'a': 14,
    'b': 15,
})

# tool binding
llm = ChatOpenAI()
tool_binding = llm.bind_tools([multiply])

query = HumanMessage('can you multiply 21 with 22 ?')

messages = [query]

res = tool_binding.invoke(messages)
# print(f"res: {res}")

messages.append(res)

# get tool message
tool_content = res.tool_calls[0]
tool_res = multiply.invoke(tool_content)
# print(f"tool result: {tool_res}")

messages.append(tool_res)
# print(f"messgaes: {messgaes}")

# send messages to LLM
final_res = tool_binding.invoke(messages)
# print(f"res: {final_res}")

print(f"res_content: {final_res.content}")