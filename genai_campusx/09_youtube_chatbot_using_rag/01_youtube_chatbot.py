
# youtube chatbot using RAG

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
)

prompt_template = PromptTemplate(
    template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
    """,
    input_variables=['context', 'question']
)


def fetch_transcript(video_id):
    # youtube-transcript-api 1.x uses an instance method named fetch()
    transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    return " ".join(chunk.text for chunk in transcript_list)


def create_vector_store(video_id="zjkBMFhNj_g"):
    # step 1 - indexing (document ingestion)
    transcript = fetch_transcript(video_id)

    # step 1.1 - indexing (text splitting)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    # step 1.2 - indexing (embedding generation and storing in vector store)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return FAISS.from_documents(chunks, embeddings)


def create_retriever(video_id="zjkBMFhNj_g"):
    vector_store = create_vector_store(video_id)
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )


if __name__ == "__main__":
    try:
        # step 2 - retrieval
        retriever = create_retriever()

        question = "is the topic of AI Agent discussed in this video? if yes then what was discussed"
        retrieved_docs = retriever.invoke(question)
        context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

        # step 3.2 - prepare final prompt
        final_prompt = prompt_template.invoke({"context": context_text, "question": question})

        # step 4 - generation
        answer = llm.invoke(final_prompt)
        print(f"final answer: {answer.content}")

    except TranscriptsDisabled:
        print("No captions available for this video")
