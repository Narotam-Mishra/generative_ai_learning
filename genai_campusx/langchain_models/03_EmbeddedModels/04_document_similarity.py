
# Document Similarity Application

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv(override=True)

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=300,
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

user_query = "Tell me about Rohit Sharma"

# find document embedding (set of 5 vectors)
doc_embedding = embedding.embed_documents(documents)

# find user's query embedding (give single vector)
query_embedding = embedding.embed_query(user_query)

# find cosine similarity between single vector and set of 5 vectors
# pass query's embedding in 2D list
# document's embedding is already in 2D list
similarity_score = cosine_similarity([query_embedding], doc_embedding)[0]

# print(f"Similarity Score: {similarity_score}")

# print similarity scores in 1D list
# print("Similarity scores in list:", list(enumerate(similarity_score)))

# sort on the basis of 2nd argument
# print("Similarity scores in sorted list:", sorted(list(enumerate(similarity_score)), key=lambda x:x[1]))

# extract last score
# print("Last score:", sorted(list(enumerate(similarity_score)), key=lambda x:x[1])[-1])

# get index and score
index, score = sorted(list(enumerate(similarity_score)), key=lambda x:x[1])[-1]
print(f"User Query: {user_query}")
print("Document item:", documents[index])
print("Similarity score of matched item:", score)
