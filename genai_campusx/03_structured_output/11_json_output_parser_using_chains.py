
# JSON Output Parser using chains

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

# create prompt template
prompt_template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = prompt_template | model | parser

res = chain.invoke({'topic': 'black hole'})

print(f"Output: {res}")
print(f"Type: {type(res)}")
