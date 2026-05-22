
# Runnable Parallel

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv(override=True)

prompt_template1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt_template2 = PromptTemplate(
    template='Generate a linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt_template1, model, parser),
    'linkedin': RunnableSequence(prompt_template2, model, parser)
})

res = parallel_chain.invoke({
    'topic': 'AI'
})

# print(f"final result: {res}")

print(f"tweet: {res['tweet']}")
print(f"linkedin post: {res['linkedin']}")