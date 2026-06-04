
# embedding model using openai

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=100,
)

res = embedding.embed_query("Delhi is the capital of India")

print(f"Embedding Response: {str(res)}")