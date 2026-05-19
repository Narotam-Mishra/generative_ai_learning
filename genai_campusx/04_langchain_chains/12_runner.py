from importlib import import_module


DummyLLM = import_module("10_llm_component").DummyLLM
DummyPromptTemplate = import_module("11_prompt_template_component").DummyPromptTemplate

template = DummyPromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

prompt = template.format({
    "length": "short",
    "topic": "India"
})

print(prompt)

llm = DummyLLM()

print(llm.predict(prompt))
