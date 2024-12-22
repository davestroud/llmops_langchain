# __init__.py

import os
import logging
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Expose configurations as part of the package
langchain_config = load_config(os.path.join(os.path.dirname(__file__), 'langchain_config.yaml'))
model_config = load_config(os.path.join(os.path.dirname(__file__), 'model_config.yaml'))
aws_secrets = load_config(os.path.join(os.path.dirname(__file__), 'aws_secrets.yaml'))
logging_config = load_config(os.path.join(os.path.dirname(__file__), 'logging_config.yaml'))
