
# Contextual Compression Retriever

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from dotenv import load_dotenv

load_dotenv(override=True)

# recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]

# create a FAISS vector store from the documents
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embedding_model)

base_retriever = vector_store.as_retriever(
    search_kwargs={"k":5}
)

# setup the compressor using LLM
llm = ChatOpenAI(model="gpt-4")
compressor = LLMChainExtractor.from_llm(llm)

# create the contextual compressor retriever
compressor_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor,
)

# query retriever
query = "What is photosynthesis?"
compressed_results = compressor_retriever.invoke(query)

# print(f"Results: {compressed_results}")

for i, doc in enumerate(compressed_results):
    print(f"\n--- Result {i+1} ---")
    print(f"content: {doc.page_content}")