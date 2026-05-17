
# document reader

from dotenv import load_dotenv
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings, OpenAI

# Load environment variables from .env file
load_dotenv(override=True)

# Load the document
pdf_path = Path(__file__).parent / "JWT-Advanced.pdf"
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Convert text into embeddings & store in FAISS
embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# Create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# Manually retrieve relevant documents
query = "What are the key takeaways from the document?"

retrieved_docs = retriever.invoke(query)

# Combine retrieved text into a single prompt
retrieved_text = "\n".join(
    [doc.page_content for doc in retrieved_docs]
)

# Initialize the LLM
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.7
)

# Manually pass retrieved text to LLM
prompt = f"""
Based on the following text, answer the question.

Question:
{query}

Context:
{retrieved_text}
"""

# Generate response
answer = llm.invoke(prompt)

# Print the answer
print("Answer:\n")
print(answer)
