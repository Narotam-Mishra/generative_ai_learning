
# RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv(override=True)

# define utility method
def word_counter(text):
    return len(text.split())

# convert method to runnable lambda
runnable_word_counter = RunnableLambda(word_counter)

# define prompt
prompt_template1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

res = runnable_word_counter.invoke('Hi there, How are you?')

# print(f"output: {res}")

# initialize llm model
model = ChatOpenAI()

# create output parser
parser = StrOutputParser()

# create joke generator chain
joke_gen_chain = RunnableSequence(prompt_template1, model, parser)

# create parallel chain
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter) 
})

# create final chain using joke generator and parallel chains
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# invoke chain
res = final_chain.invoke({
    'topic': 'Indian Premier League'
})

# print(f"Output: {res}")

print(f"Joke: {res['joke']} \n")
print(f"Joke's word count:: {res['word_count']}")