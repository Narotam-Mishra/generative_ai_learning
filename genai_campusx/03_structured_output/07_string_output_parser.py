
# string output parser

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

# 1st prompt --> Detailed report
prompt_template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt --> summary
prompt_template2 = PromptTemplate(
    template='Write 5 line summary on the following text. \n {text}',
    input_variables=['text']
)

prompt1 = prompt_template1.invoke({'topic': 'black hole'})
res1 = model.invoke(prompt1)

prompt2 = prompt_template2.invoke({'text': res1.content})
res2 = model.invoke(prompt2)

print(f"Output: {res2.content}")