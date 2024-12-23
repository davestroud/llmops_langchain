import os
from langsmith.client import LangSmithClient

api_key = os.getenv("LANGSMITH_API_KEY")
client = LangSmithClient(api_key=api_key)

def log_chain_performance(chain_name, latency, token_usage):
    client.log_metric(chain_name, "latency", latency)
    client.log_metric(chain_name, "token_usage", token_usage)
    print(f"Logged chain metrics for {chain_name}")

def log_error(chain_name, error_message):
    client.log_event(chain_name, "error", {"message": error_message})
    print(f"Logged error for {chain_name}")
