
# string output parser

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

# pipeline (chain)
chain = prompt_template1 | model | parser | prompt_template2 | model | parser

res = chain.invoke({'topic': 'black hole'})
print(f"output: {res}")