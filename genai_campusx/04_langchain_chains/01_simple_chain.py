
# simple chain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

# step 1 - prepare prompt
prompt_template = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# step 2 - create instance of openai's model
model = ChatOpenAI()

# step 3 - create output parser
parser = StrOutputParser()

# step 4 - form chain 
chain = prompt_template | model | parser

# tigger the chain
res = chain.invoke({'topic': 'Cricket'})

print(f"Output: {res}")

# visualize chain
chain.get_graph().print_ascii()

