
# retrieval QA Chain

# retrievalQAchain.py

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# ---------------------------------------------------
# Load environment variables
# ---------------------------------------------------
load_dotenv(override=True)

# ---------------------------------------------------
# Step 1: Load the text document
# ---------------------------------------------------
loader = TextLoader("docs.txt")
documents = loader.load()

# ---------------------------------------------------
# Step 2: Split document into chunks
# ---------------------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# ---------------------------------------------------
# Step 3: Create embeddings and store in FAISS
# ---------------------------------------------------
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# ---------------------------------------------------
# Step 4: Create Retriever
# ---------------------------------------------------
retriever = vectorstore.as_retriever()

# ---------------------------------------------------
# Step 5: Initialize LLM
# ---------------------------------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# ---------------------------------------------------
# Step 6: Build the LCEL QA Chain
# ---------------------------------------------------
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:
{context}

Question: {question}
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ---------------------------------------------------
# Step 7: Ask a question and print the answer
# ---------------------------------------------------
query = "What are the key takeaways from the document?"
answer = qa_chain.invoke(query)

print("Answer:")
print(answer)