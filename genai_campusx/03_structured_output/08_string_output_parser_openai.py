
# string output parser

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv(override=True)

model = ChatOpenAI()

# 1st prompt --> Detailed report
prompt_template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variable=['topic']
)

# 2nd prompt --> summary
prompt_template2 = PromptTemplate(
    template='Write a five line summary on the following text \n {text}',
    input_variable=['text']
)

prompt1 = prompt_template1.invoke({'topic': 'black hole'})
res1 = model.invoke(prompt1)

prompt2 = prompt_template2.invoke({'text': res1.content})
res2 = model.invoke(prompt2)

print(f"Output: {res2.content}")