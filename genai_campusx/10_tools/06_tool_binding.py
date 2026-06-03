
# example code to explain tool binding

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# create tool
@tool
def multiply(a: int, b: int) -> int:
    """Given two numbers a and b this tool returns their product"""
    return a * b

res = multiply.invoke({
    'a': 14,
    'b': 15,
})

# print(f"multiplication result: {res}")
# print(f"tool name: {multiply.name}")
# print(f"tool description: {multiply.description}")
# print(f"tool args: {multiply.args}")

# tool binding
llm = ChatOpenAI()
tool_binding = llm.bind_tools([multiply])

# print(f"tool binding: {tool_binding}")