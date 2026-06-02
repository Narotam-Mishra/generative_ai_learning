
# custom tools

from langchain_core.tools import tool

# step 1 - create a function
def multiply(a,b):
    """multiply two numbers"""
    return a * b

# step 2 - add type hints
def multiply(a:int, b:int) -> int:
    """multiply two numbers"""
    return a * b

# step 3 - add tool decorator
@tool
def multiply(a:int, b:int) -> int:
    """multiply two numbers"""
    return a * b

# invoke tool
res = multiply.invoke({"a":12,"b":13})
print(f"res: {res}")

print(f"tool name: {multiply.name}")
print(f"tool description: {multiply.description}")
print(f"tool args: {multiply.args}")

print("*"*50)
print(multiply.args_schema.model_json_schema())