
# prompt template component class

class DummyPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
if __name__ == "__main__":
    template = DummyPromptTemplate(
        template='Write a {length} Poem about {topic}',
        input_variables=['length', 'topic']
    )

    print(template.format({'length': 'short', 'topic': 'India'}))
