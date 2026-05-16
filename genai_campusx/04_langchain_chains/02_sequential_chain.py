
# sequential chain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

prompt_template1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt_template2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt_template1 | model | parser | prompt_template2 | model | parser

res = chain.invoke({'topic': 'Unemployment in India'})

print(f"Output: {res}")

chain.get_graph().print_ascii()