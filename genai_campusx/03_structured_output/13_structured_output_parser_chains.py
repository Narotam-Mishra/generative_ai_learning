
# structured output parser using chains

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema  

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation',
)
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)  # ✅ was: from_response_schema (missing 's')

prompt_template = PromptTemplate(
    template='Give 3 facts about {topic}\n{format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}  # ✅ was: get_format_instruction (missing 's')
)

chain = prompt_template | model | parser

res = chain.invoke({'topic': 'black hole'})

print(f"Output: {res}")