import random
from abc import ABC, abstractmethod

class Runnable(ABC):

    @abstractmethod
    def invoke(self, input_data):
        pass

class DummyLLM(Runnable):
    def __init__(self):
        print("LLM created...")

    def invoke(self, prompt):
        if "Explain" in prompt:
            return {
                'response': 'The joke is funny because it connects programming bugs with everyday debugging.'
            }

        if "joke" in prompt:
            return {
                'response': 'Why did the programmer go broke? Because he used up all his cache.'
            }

        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stand for Artificial Intelligence'
        ]

        return {
            'response': random.choice(response_list)
        }

    def predict(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stand for Artificial Intelligence'
        ]

        return {
            'response': random.choice(response_list)
        }
    
class DummyPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        if not isinstance(input_dict, dict) and len(self.input_variables) == 1:
            input_dict = {
                self.input_variables[0]: input_dict
            }

        return self.template.format(**input_dict)

    def format(self, input_dict):
        if not isinstance(input_dict, dict) and len(self.input_variables) == 1:
            input_dict = {
                self.input_variables[0]: input_dict
            }

        return self.template.format(**input_dict)

class DummyStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']


    
class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data


if __name__ == "__main__":
    llm = DummyLLM()
    parser = DummyStrOutputParser()

    prompt1 = DummyPromptTemplate(
        template="Write a joke about {topic}",
        input_variables=['topic']
    )

    prompt2 = DummyPromptTemplate(
        template="Explain the following joke {response}",
        input_variables=['response']
    )

    input_data = {
        "topic": "programming"
    }

    joke_chain = RunnableConnector([prompt1, llm, parser])
    explanation_chain = RunnableConnector([prompt2, llm, parser])

    final_chain = RunnableConnector([joke_chain, explanation_chain])
    
    print("Joke:")
    joke = joke_chain.invoke(input_data)
    print(joke)

    print("\nExplanation:")
    explanation = explanation_chain.invoke({
        "response": joke
    })
    print(explanation)

    print("\nFinal Chain Output:")
    final_output = final_chain.invoke(input_data)
    print(final_output)
