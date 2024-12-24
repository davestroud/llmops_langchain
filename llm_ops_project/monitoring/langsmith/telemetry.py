import os
import logging
from langsmith.client import LangSmithClient

# Retrieve the LangSmith API key from the environment
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")

client = LangSmithClient(api_key=langsmith_api_key)
logger = logging.getLogger(__name__)

def track_latency(chain_name, start_time, end_time):
    latency = end_time - start_time
    client.log_metric(chain_name, "latency", latency)
    logger.info(f"Latency for {chain_name}: {latency}s")
