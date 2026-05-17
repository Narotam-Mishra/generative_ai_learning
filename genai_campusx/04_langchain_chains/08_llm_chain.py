
# LLM Chains

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv(override=True)

# step 1 - Load the LLM (GPT-3.5)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)

# step 2 - create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# step 3 - Build the chain using LCEL (LangChain Expression Language)
chain = prompt | llm | StrOutputParser()

# step 4 - Run the chain with a specific topic
topic = input("Enter a topic: ")
output = chain.invoke({"topic": topic})

print("Generated Blog Title:", output)