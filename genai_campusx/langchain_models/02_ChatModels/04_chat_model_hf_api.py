
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("Is Arunachal Pradesh belongs to India or China?")
print(f"Response:\n {res.content}")