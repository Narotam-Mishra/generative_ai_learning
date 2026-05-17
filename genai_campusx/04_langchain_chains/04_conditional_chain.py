
# conditional chains

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv(override=True)

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

# prepare prompt
prompt_template1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': pydantic_parser.get_format_instructions()}
)

classifier_chain = prompt_template1 | model | pydantic_parser

# res = classifier_chain.invoke({'feedback': 'this is just a terrible smartphone'})
# print(f"Output: {res.sentiment}")

prompt_template2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt_template3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# create branch
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_template2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt_template3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

# chain classifier and branch into one chain
chain = classifier_chain | branch_chain

res = chain.invoke({'feedback': 'this is a wonderful phone'})
print(f"Output: {res}")

# visualize chain
chain.get_graph().print_ascii()