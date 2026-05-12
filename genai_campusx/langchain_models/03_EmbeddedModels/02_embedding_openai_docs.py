# multiple embedding (for documents)

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=100,
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is capital of France"
]

res = embedding.embed_documents(documents)

print(f"Embedding Response: {str(res)}")