import logging
import yaml
import os
from logging.config import dictConfig

def setup_logger(name):
    config_path = "config/logging_config.yaml"
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    dictConfig(config)
    logger = logging.getLogger(name)
    return logger 