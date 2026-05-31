
import importlib.util
from pathlib import Path

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


def load_youtube_chatbot_objects():
    module_path = Path(__file__).with_name("01_youtube_chatbot.py")
    spec = importlib.util.spec_from_file_location("youtube_chatbot_01", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.create_retriever, module.prompt_template, module.llm

def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text


create_retriever, prompt_template, llm = load_youtube_chatbot_objects()
retriever = create_retriever()

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt_template | llm | parser

query = "Can you Summaries the video?"
res = main_chain.invoke(query)

print(f"final result: {res}")
