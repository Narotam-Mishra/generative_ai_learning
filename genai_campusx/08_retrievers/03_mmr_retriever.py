
# MMR Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv(override=True)

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# step 1 - intialize OpenAI embeddings
embedding_model = OpenAIEmbeddings()

# step 2 - create the FAISS vector store from documents
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model,
)

# step 3 - enable MMR in the retriever
retriever = vector_store.as_retriever(
    search_type="mmr",                       # <-- This enables MMR
    search_kwargs={"k":3, "lambda_mult":0.5} # k = top results, lambda_mult = relevance-diversity balance
)

# enter your query
query = "What is Langchain?"
results = retriever.invoke(query)

# print(f"Results: {results}")

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content: {doc.page_content}")