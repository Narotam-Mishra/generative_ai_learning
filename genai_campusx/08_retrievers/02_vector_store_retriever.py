
# Vector Store Retriever

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv(override=True)

# step 1 - add your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# step 2 - initialize embedding model
embedding_model = OpenAIEmbeddings()

# step 3 - create Chroma vector store in memory
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# step 4 - convert vector store into retriever
retriever = vector_store.as_retriever(search_kwargs={"k":2})

# enter your query
query = "What is Chroma used for?"
results = retriever.invoke(query)

# without retriever
# res = vector_store.similarity_search(query, k=2)

# print(f"Results: {results}")
# print(f"result: {res}")

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content: {doc.page_content}")