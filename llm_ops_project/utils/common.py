import os
from dotenv import load_dotenv
from langsmith.client import LangSmithClient

# Load environment variables
load_dotenv()

def get_langsmith_client():
    api_key = os.getenv("LANGSMITH_API_KEY")
    return LangSmithClient(api_key=api_key) 