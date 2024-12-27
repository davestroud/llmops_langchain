class ChainBuilder:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def build_chain(self):
        # Example function to build an LLM chain
        return {"llm": self.llm, "prompt_template": self.prompt_template}
