import logging
from llm_ops_project.utils.common import get_langsmith_client

client = get_langsmith_client()
logger = logging.getLogger(__name__)

def track_latency(chain_name, start_time, end_time):
    latency = end_time - start_time
    client.log_metric(chain_name, "latency", latency)
    logger.info(f"Latency for {chain_name}: {latency}s")
