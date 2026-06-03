
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

res = tool_binding.invoke('can you multiply 16 with 17 ?')
# print(f"zeroth item: {res.tool_calls[0]}")

# tool execution flow

# tool_args = res.tool_calls[0]['args']
# final_res = multiply.invoke(tool_args)
# print(f"res: {final_res}")

# get tool message
tool_content = res.tool_calls[0]
final_res = multiply.invoke(tool_content)
print(f"res: {final_res}")