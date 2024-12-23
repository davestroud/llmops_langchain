import os
from langsmith.client import LangSmithClient

# Retrieve API keys and environment variables from the environment
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")

# Initialize the LangSmith client
client = LangSmithClient(api_key=langsmith_api_key)

def log_chain_performance(chain_name, latency, token_usage):
    client.log_metric(chain_name, "latency", latency)
    client.log_metric(chain_name, "token_usage", token_usage)
    print(f"Logged chain metrics for {chain_name}")

def log_error(chain_name, error_message):
    client.log_event(chain_name, "error", {"message": error_message})
    print(f"Logged error for {chain_name}")
