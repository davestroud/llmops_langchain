import pinecone
from langchain.embeddings import OpenAIEmbeddings
import yaml
import os

class PineconeHandler:
    def __init__(self, index_name):
        self.index_name = index_name
        self.load_config()
        self.init_pinecone()
        self.embeddings = OpenAIEmbeddings()
    
    def load_config(self):
        with open("config/langchain_config.yaml", 'r') as f:
            self.config = yaml.safe_load(f)['embeddings']
    
    def init_pinecone(self):
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENV")
        )
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(
                name=self.index_name,
                dimension=1536,  # OpenAI embedding dimension
                metric="cosine"
            )
        self.index = pinecone.Index(self.index_name) 