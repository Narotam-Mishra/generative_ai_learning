
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

# initialize the LLM
llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=0.7,
)

# create prompt template
prompt_template = PromptTemplate(
    template='Suggest a catchy blog title about {topic}',
    input_variables=['topic'],
)

# define the input
topic = input('Enter a topic: ')

# format the prompt manually using PromptTemplate
formatted_prompt = prompt_template.format(topic=topic)

# call LLM directly
blog_title = llm.invoke(formatted_prompt)

# print output
print(f"Generated blog title: {blog_title}")