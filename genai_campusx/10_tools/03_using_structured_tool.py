
# using StructuredTool class

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="first number to add")
    b: int = Field(required=True, description="second number to add")

def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="multiply two numbers",
    args_schema=MultiplyInput,
)

res = multiply_tool.invoke({
    'a': 13,
    'b': 14,
})

print(f"res: {res}")
print(f"tool_name: {multiply_tool.name}")
print(f"tool_description: {multiply_tool.description}")
print(f"tools args: {multiply_tool.args}")