from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import yaml
import os

class LLMClient:
    def __init__(self, model_name="gpt-4"):
        self.load_config()
        self.model = ChatOpenAI(
            model_name=model_name,
            **self.model_config.get(model_name, {})
        )
    
    def load_config(self):
        config_path = "config/model_config.yaml"
        with open(config_path, 'r') as f:
            self.model_config = yaml.safe_load(f)['models']
    
    async def generate(self, prompt, system_message=None):
        messages = []
        if system_message:
            messages.append(SystemMessage(content=system_message))
        messages.append(HumanMessage(content=prompt))
        
        try:
            response = await self.model.agenerate([messages])
            return response.generations[0][0].text
        except Exception as e:
            raise Exception(f"Error generating response: {str(e)}") 