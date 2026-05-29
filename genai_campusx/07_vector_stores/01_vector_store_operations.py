
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

CURRENT_DIR = Path(__file__).parent

# create LangChain documents for IPL players
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"}
)

doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"}
)

doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"}
)

# form list using above document objects
docs = [doc1, doc2, doc3, doc4, doc5]
doc_ids = ["virat_kohli", "rohit_sharma", "ms_dhoni", "jasprit_bumrah", "ravindra_jadeja"]

# intialize vector store
vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory=str(CURRENT_DIR / 'my_chroma_db'),
    collection_name='sample',
)

# add documents to vector store
res = vector_store.add_documents(documents=docs, ids=doc_ids)

# print(f"vector embeddings: {res}")

# view documents
# val = vector_store.get(include=['embeddings','documents','metadatas'])
# print(f"view documents: {val}")

# search documents using similarity search
# ans = vector_store.similarity_search(
#     query='Who among these are bowlers?',
#     k=2,
# )

# similarity score
# ans = vector_store.similarity_search_with_score(
#     query='Who among these are bowlers?',
#     k=2,
# )

# meta-data filtering
# ans = vector_store.similarity_search_with_score(
#     query='',
#     k=2,
#     filter={
#         "team": "Chennai Super Kings"
#     }
# )

# print(f"bowlers: {ans}")

# update documents
# updated_doc1 = Document(
#     page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
#     metadata={"team": "Royal Challengers Bangalore"}
# )

# vector_store.update_document(document_id='virat_kohli', document=updated_doc1)

# delete document
# vector_store.delete(ids=['ravindra_jadeja'])

# verify delete
# deleted_doc = vector_store.get(ids=['ravindra_jadeja'], include=['documents','metadatas'])
# print(f"deleted document lookup: {deleted_doc}")

remaining_docs = vector_store.get(include=['embeddings', 'documents','metadatas'])
print(f"remaining documents: {remaining_docs}")
