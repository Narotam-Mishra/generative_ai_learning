
# building AI Agent from scratch

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import AgentExecutor, create_react_agent
from langsmith import Client
import requests
import os

load_dotenv(override=True)

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('top news in India today')

# print(f"search result: {results}")

llm = ChatOpenAI()

# res = llm.invoke('Hi, Tell who is better at Reasoning ChatGPT or Deepseek?')
# print(f"res: {res}")

# step 2 - pull the ReAct prompt from LangChain Hub
client = Client()
prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)
# print(f"prompt: {prompt}")

# step 3 - create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt,
)

# step 4 - wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True,
) 

# step 5 - invoke
response = agent_executor.invoke({
    'input': "give 5 pointer preview for IPL final of 2026"
})

# print(f"response: {response}")
print(f"response_output: {response['output']}")
