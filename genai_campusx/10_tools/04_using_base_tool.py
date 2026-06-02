
# using BaseTool class

from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# arg schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="first number to add")
    b: int = Field(required=True, description="second number to add")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b
    

multiply_tool = MultiplyTool()

res = multiply_tool.invoke({
    'a': 22,
    'b': 21,
})

print(f"res: {res}")
print(f"tool_name: {multiply_tool.name}")
print(f"tool_description: {multiply_tool.description}")
print(f"tool_args: {multiply_tool.args}")