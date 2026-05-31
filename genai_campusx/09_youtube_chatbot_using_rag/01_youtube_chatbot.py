
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# step 1 - indexing (document ingestion)
video_id = "zjkBMFhNj_g"
try:
    # youtube-transcript-api 1.x uses an instance method named fetch()
    transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=["en"])

    # flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(f"Video Transcript: {transcript}")
    print(f"Video Transcript first 800 words: {' '.join(transcript.split()[:800])}")

except TranscriptsDisabled:
    print("No captions available for this video")
