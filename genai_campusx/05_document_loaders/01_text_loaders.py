
# text document loader

from langchain_community.document_loaders import TextLoader

# create document loader object
loader = TextLoader('cricket.txt', encoding="utf-8")
docs = loader.load()

# load the document
docs = loader.load()

# print(f"Document's content: {docs}")

# print(f"Lenght of document: {len(docs)}")

# print(f"Content of document: {docs[0]}")

print(f"Type of document content: {type(docs[0])}")