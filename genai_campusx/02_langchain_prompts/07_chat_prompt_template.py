
# chat prompt templates (for multi turn conversations)

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}?'),
])

prompt = chat_template.invoke({
    'domain': 'Artificial Intelligence',
    'topic': 'Agentic AI'
})

print(f"Prompt: {prompt}")