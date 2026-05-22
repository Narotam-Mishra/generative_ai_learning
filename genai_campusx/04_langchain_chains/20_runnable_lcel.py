
# RunnableSequence example

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

# define prompt
prompt_template1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt_template2 = PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']
)


# initialize llm model
model = ChatOpenAI()

# create output parser
parser = StrOutputParser()

# create runnable sequence and chain them
# using LCEL
chain = prompt_template1 | model | parser | prompt_template2 | model | parser

# invoke chain
res = chain.invoke({
    'topic': 'AI'
})

print(f"final result: {res}")
