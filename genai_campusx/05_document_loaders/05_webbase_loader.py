
# web base loader

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

# set a custom user agent for web requests
os.environ["USER_AGENT"] = "genai-learning/1.0"  

model = ChatOpenAI()

prompt_template = PromptTemplate(
    template='Answer the following questions - \n {question} from the following text - \n {text}',
    input_variables=['text','question']
)

parser = StrOutputParser()


url = 'https://www.amazon.in/Apple-MacBook-15-inch-10-core-Unified/dp/B0DZDG4RMG/ref=sr_1_1_sspa?adgrpid=166137947670&dib=eyJ2IjoiMSJ9.IH7ekYjEFZw8JIQA4mxDuWIbovwmBCROTXxkB40tQcMPZIgy0bmoJZDz9TqGVN_WrdRhBGqSKAIZvI4EuBPqeuW9JhabpS7sCROYPCMK7I8n4SxH2VzI8Qt31sdahm0u0Gl6B_AF2DOc4hqXhbTVkwUjeyaKuFLLGieKZbOONJkCnBC695JxluRK2xIAQrYrmz-P_UboRi0pKcLJpXkGUDISfYrrIij7yGSxqxPmxBY.Fzm2pZVvjB6MpsQhT0__PyTH7YpuHnEpNu0rF_WntDU&dib_tag=se&gad_source=1&hvadid=699321259915&hvdev=c&hvexpln=0&hvlocphy=9061996&hvnetw=g&hvocijid=16802162091749369137--&hvqmt=e&hvrand=16802162091749369137&hvtargid=kwd-2248778423457&hydadcr=24569_2265455&keywords=macbook%2Bm4%2Bpro&mcid=141f7747b7a03b749efa9e4c175e9fcd&qid=1779625990&sr=8-1-spons&aref=9xyTxnswK6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt_template | model | parser

res = chain.invoke({
    'question': 'what are core features of this product',
    'text': docs[0].page_content
})

print(f"Answer: {res}")