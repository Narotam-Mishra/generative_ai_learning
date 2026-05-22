
# RunnableBranch

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv(override=True)

prompt_template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt_template2 = PromptTemplate(
    template='Summaries the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

# create report generation chain
report_gen_chain = RunnableSequence(prompt_template1, model, parser)

# create branch chain
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 200, RunnableSequence(prompt_template2, model, parser)),
    RunnablePassthrough(),
)

# create final chain from report generation and branch chain
final_chain = RunnableSequence(report_gen_chain, branch_chain)

res = final_chain.invoke({
    'topic': 'Russia vs Ukraine war',
})

print(f"output: {res}")