
# Length based Text Splitting

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

# create splitter object
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

# res = splitter.split_text(text)

res = splitter.split_documents(docs)

# print(f"split chunks: {res}")

# print(f"length of split chunks: {len(res)}")

print(f"extract first chunk page content: {res[0].page_content}")