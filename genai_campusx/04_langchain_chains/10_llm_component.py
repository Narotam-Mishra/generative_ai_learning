
# LLM component class

import random

class DummyLLM:
    def __init__(self):
        print("LLM created...")

    def predict(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stand for Artificial Intelligence'
        ]

        return {
            'response': random.choice(response_list)
        }
    
if __name__ == "__main__":
    llm = DummyLLM()
    print(llm.predict('what is the capital of India'))
