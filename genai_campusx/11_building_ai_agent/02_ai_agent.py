
# building AI Agent (contd...)

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import AgentExecutor, create_react_agent
from langsmith import Client
import requests
import os

load_dotenv(override=True)

weather_api_key = os.getenv('WEATHER_API_KEY')

# step 1 - use tool
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str):
    """
    this function fetches the current weather data for a given city
    """
    url = f"https://api.weatherstack.com/current?access_key={weather_api_key}&query={city}"

    response = requests.get(url)

    return response.json()


llm = ChatOpenAI()


# step 2 - pull the ReAct prompt from LangChain Hub
client = Client()
prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)
# print(f"prompt: {prompt}")

# step 3 - create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt,
)

# step 4 - wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True,
) 

# step 5 - invoke
response = agent_executor.invoke({
    'input': "Find the capital of Karnataka, then find it's current weather condition"
})

# print(f"response: {response}")
print(f"response_output: {response['output']}")
