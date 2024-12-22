from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Initialize LLM
llm = OpenAI(model_name="text-davinci-003", api_key="your-openai-api-key")

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short essay about {topic}."
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the chain
output = chain.run({"topic": "machine learning operations"})
print(output)
