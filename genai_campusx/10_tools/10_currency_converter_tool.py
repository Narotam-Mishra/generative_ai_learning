
# currency converter tool

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from typing import Annotated
import os
import requests
import json

load_dotenv(override=True)

cc_api_key = os.getenv("CURRENCY_CONVERSION_API_KEY")

# create tool
@tool
def get_conversion_factor(base_currency:str, target_currency: str) -> float:
    """this function fetches the currency conversion fator between a given base currency and target currency"""
    url = f"https://v6.exchangerate-api.com/v6/{cc_api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    return response.json()

res = get_conversion_factor.invoke({
    'base_currency': 'USD',
    'target_currency': 'INR',
})

# print(f"res: {res}")

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    """
    return base_currency_value * conversion_rate


res = convert.invoke({
    'base_currency_value': 12,
    'conversion_rate': 95.3411,
})

# print(f"Rs(INR): {res}")

# bind tools with LLM
llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

# tool calling
messages = [HumanMessage('What is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr?')]

# print(f"messgaes: {messages}")

ai_message = llm_with_tools.invoke(messages)
# print(f"tool call: {ai_message.tool_calls}")
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    # execute the first tool and get the value of conversion rate
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
        # print(f"tool messgae 1: {tool_message1}")

        # fetch conversion rate
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        # print(f"tool message1 conversion rate: {json.loads(tool_message1.content)['conversion_rate']}")

        # then append this tool messgae to messages list
        messages.append(tool_message1)
    # execute the second tool using the conversion rate from tool 1
    if tool_call['name'] == 'convert':
        # fetch the current argument
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)
    
# print(f"messages: {messages}")

final_res = llm_with_tools.invoke(messages)
# print(f"final res: {final_res}")
print(f"final res content: {final_res.content}")