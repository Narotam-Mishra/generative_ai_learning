
# pdf loader

from langchain_community.document_loaders import PyPDFLoader

# create instance of pdf loader
loader = PyPDFLoader('Deep Learning Curriculum.pdf')

# load pdf document
pdf_docs = loader.load()

# print(f"PDF Content: {pdf_docs}")

# print(f"Lenght of PDF list: {len(pdf_docs)}")

print(f"Page Content: {pdf_docs[0].page_content}")
print(f"Meadata: {pdf_docs[1].metadata}")
