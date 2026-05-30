
# Wikipedia Retriever

from langchain_community.retrievers import WikipediaRetriever
import wikipedia

# initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")

# The wikipedia==1.4.0 package still defaults to http://... for its API URL.
# Wikipedia now expects HTTPS, so force the client to use the HTTPS endpoint.
wikipedia.wikipedia.API_URL = wikipedia.wikipedia.API_URL.replace("http://", "https://", 1)
wikipedia.set_user_agent("genai-campusx-learning/1.0")

# define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# get relevant Wikipedia documents
docs = retriever.invoke(query)

# print(f"query response: {docs}")

# print retrieved content
for i, doc in enumerate(docs):
    print(f"\n---- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")
