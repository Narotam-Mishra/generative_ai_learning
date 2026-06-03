
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

res = tool_binding.invoke('can you multiply 16 with 17 ?')
# print(f"res: {res.tool_calls}")
print(f"zeroth item: {res.tool_calls[0]}")