
# using built-in tools

# using DuckDuckGoSearch

from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

search_tool = DuckDuckGoSearchRun()

shell_tool = ShellTool()

results = search_tool.invoke('top news in India today')

res = shell_tool.invoke('whoami')

print(f"result: {results}")
print("*"*60)
print(f"shell command whoami: {res}")