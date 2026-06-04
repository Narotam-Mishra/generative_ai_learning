
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# text = "Mumbai is the financial capital of India"

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is capital of France"
]

vector = embedding.embed_documents(documents)

print(f"Vectors for given text:\n {vector}")