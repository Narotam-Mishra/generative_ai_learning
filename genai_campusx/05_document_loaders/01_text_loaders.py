
# text document loader

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatOpenAI()

prompt_template = PromptTemplate(
    template='Write a summary for the following - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

# create document loader object
loader = TextLoader('cricket.txt', encoding="utf-8")

# load the document
docs = loader.load()

# print(f"Document's content: {docs}")

# print(f"Type of Document : {type(docs)}")

# print(f"Lenght of document: {len(docs)}")

# print(f"Content of document: {docs[0]}")

# print(f"Type of document content: {type(docs[0])}")

print(f"Content of document: {docs[0].page_content}")
# print(f"Metadata of document: {docs[0].metadata}")

chain = prompt_template | model | parser

res = chain.invoke({
    'poem': docs[0].page_content
})

print(f"Poem Summary: {res}")