
# LLM Chain Component

from importlib import import_module

DummyLLM = import_module("10_llm_component").DummyLLM
DummyPromptTemplate = import_module("11_prompt_template_component").DummyPromptTemplate

class DummyLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        res = self.llm.predict(final_prompt)
        return res['response']


if __name__ == "__main__":
    llm = DummyLLM()

    prompt = DummyPromptTemplate(
        template="Write a {length} poem about {topic}",
        input_variables=["length", "topic"]
    )

    chain = DummyLLMChain(llm=llm, prompt=prompt)

    result = chain.run({
        "length": "short",
        "topic": "India"
    })

    print(result)
