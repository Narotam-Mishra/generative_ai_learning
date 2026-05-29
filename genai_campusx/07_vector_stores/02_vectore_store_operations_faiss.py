import os
import shutil
import uuid
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# ---------- 1. Clean previous data (for demonstration) ----------
PERSIST_DIR = "./faiss_db"
if os.path.exists(PERSIST_DIR):
    shutil.rmtree(PERSIST_DIR)

# ---------- 2. Create embedding model ----------
embeddings = OpenAIEmbeddings()

# ---------- 3. Create cricket player documents ----------
documents = [
    Document(page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history.",
             metadata={"team": "RCB"}),
    Document(page_content="Rohit Sharma is known for his elegant batting and record 5 IPL titles as captain.",
             metadata={"team": "MI"}),
    Document(page_content="MS Dhoni is famous for his calm captaincy and finishing skills. He led CSK to multiple titles.",
             metadata={"team": "CSK"}),
    Document(page_content="Jasprit Bumrah is a fast bowler with a unique action. He is a key wicket‑taker for MI.",
             metadata={"team": "MI"}),
    Document(page_content="Ravindra Jadeja is an exceptional all‑rounder, great with both bat and ball. He plays for CSK.",
             metadata={"team": "CSK"}),
]

# ---------- 4. Create vector store from documents ----------
vector_store = FAISS.from_documents(documents, embeddings)
vector_store.save_local(PERSIST_DIR)   # persist to disk

print("Documents added successfully.")

# ---------- 5. View all documents (similar to Chroma's .get()) ----------
all_data = vector_store.get()
print(f"\nTotal documents: {len(all_data['ids'])}")
print("Document IDs:", all_data['ids'])
print("Metadatas:", all_data['metadatas'])

# ---------- 6. Similarity search (without scores) ----------
query = "Who among these is a bowler?"
print("\n=== Similarity Search (k=2) ===")
results = vector_store.similarity_search(query, k=2)
for doc in results:
    print(f"- {doc.page_content}")

# ---------- 7. Similarity search with scores (lower = better) ----------
print("\n=== Similarity Search with Scores ===")
results_with_score = vector_store.similarity_search_with_score(query, k=2)
for doc, score in results_with_score:
    print(f"Score: {score:.4f} | {doc.page_content}")

# ---------- 8. Metadata filtering ----------
print("\n=== Filtered Search (team = CSK) ===")
filtered_results = vector_store.similarity_search(
    query="Who is a great all‑rounder?",
    k=2,
    filter={"team": "CSK"}
)
for doc in filtered_results:
    print(f"- {doc.page_content}")

# ---------- 9. Add a new document ----------
new_doc = Document(page_content="Hardik Pandya is a dynamic all‑rounder and captain of Gujarat Titans.",
                   metadata={"team": "GT"})
new_id = str(uuid.uuid4())                 # generate a custom ID
vector_store.add_documents([new_doc], ids=[new_id])
vector_store.save_local(PERSIST_DIR)       # persist after addition

print("\nNew document added.")

# ---------- 10. Update an existing document (FAISS has no native update – delete + add) ----------
# Find the ID of the document we want to update (Virat Kohli)
target_id = None
for i, meta in enumerate(all_data["metadatas"]):
    if meta.get("team") == "RCB":
        target_id = all_data["ids"][i]
        break

if target_id:
    # Delete the old document
    vector_store.delete(ids=[target_id])
    # Add the updated version using the same ID
    updated_doc = Document(
        page_content="Virat Kohli, the former captain of RCB, is renowned for his aggressive leadership and batting consistency.",
        metadata={"team": "RCB"}
    )
    vector_store.add_documents([updated_doc], ids=[target_id])
    vector_store.save_local(PERSIST_DIR)
    print(f"\nDocument with ID {target_id} updated successfully.")
else:
    print("\nCould not find document with team='RCB' to update.")

# ---------- 11. Delete a document (example: delete the newly added Hardik Pandya) ----------
# We can delete by ID (we already have `new_id` from earlier)
vector_store.delete(ids=[new_id])
vector_store.save_local(PERSIST_DIR)
print(f"\nDocument with ID {new_id} deleted.")

# ---------- 12. Verify final state ----------
final_data = vector_store.get()
print(f"\nFinal document count: {len(final_data['ids'])}")
print("Remaining IDs:", final_data['ids'])