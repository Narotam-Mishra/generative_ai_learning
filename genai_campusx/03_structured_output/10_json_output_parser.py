
# JSON Output Parser

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
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = prompt_template.format()

# print(f"Actual Prompt: {prompt}")

res = model.invoke(prompt)

parsed_res = parser.parse(res.content)

print(f"Output: {parsed_res}")
print(f"Type: {type(parsed_res)}")
print(f"Name: {parsed_res['name']}")