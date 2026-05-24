
# directory loader

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='ml_books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

# print(f"Docs length: {len(docs)}")

print(f"Page Content: {docs[0].page_content}")
print(f"Metadata: {docs[0].metadata}")