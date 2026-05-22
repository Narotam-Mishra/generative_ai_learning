
# RunnablePassThrough 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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

# create runnable sequence and chain them (for joke generation)
joke_gen_chain = RunnableSequence(prompt_template1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt_template2, model, parser)
})

# connect joke chain with parallel chain
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# invoke final chain
res = final_chain.invoke({
    'topic': 'Cricket'
})

# print(f"final result: {res}")

print(f"Joke: {res['joke']} \n")
print(f"Joke's Explanation: {res['explanation']} \n")