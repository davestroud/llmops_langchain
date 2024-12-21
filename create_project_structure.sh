#!/bin/bash

# Create main project directory
mkdir -p llm_ops_project

# Create directory structure
cd llm_ops_project

# Config directory
mkdir -p config
touch config/__init__.py
touch config/model_config.yaml
touch config/langchain_config.yaml
touch config/aws_secrets.yaml
touch config/logging_config.yaml

# Source directory and its subdirectories
mkdir -p src/base src/prompt_engineering src/utils src/handlers
touch src/__init__.py

# Base directory
touch src/base/__init__.py
touch src/base/llm_client.py
touch src/base/pinecone_handler.py
touch src/base/kubeflow_client.py

# Prompt engineering directory
touch src/prompt_engineering/__init__.py
touch src/prompt_engineering/templates.py
touch src/prompt_engineering/dynamic_prompts.py
touch src/prompt_engineering/chain_builder.py

# Utils directory
touch src/utils/__init__.py
touch src/utils/rate_limiter.py
touch src/utils/token_counter.py
touch src/utils/logger.py

# Handlers directory
touch src/handlers/__init__.py
touch src/handlers/error_handler.py

# Data directory and subdirectories
mkdir -p data/cache data/prompts data/outputs data/embeddings

# Examples directory
mkdir -p examples
touch examples/simple_chain.py
touch examples/kubeflow_pipeline.py
touch examples/pinecone_index.py

# Notebooks directory
mkdir -p notebooks
touch notebooks/langchain_testing.ipynb
touch notebooks/pipeline_experiments.ipynb
touch notebooks/embeddings_analysis.ipynb

# Infrastructure directory
mkdir -p infra/terraform infra/docker infra/kubeflow

# Monitoring directory
mkdir -p monitoring/langsmith
touch monitoring/aws_cloudwatch.py
touch monitoring/prometheus_config.yaml

# Tests directory
mkdir -p tests/unit tests/integration

# GitHub workflows directory
mkdir -p .github/workflows
touch .github/workflows/deploy.yml
touch .github/workflows/lint_and_test.yml

# Root level files
touch requirements.txt
touch README.md
touch Dockerfile
touch setup.py 