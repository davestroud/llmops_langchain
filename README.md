# LLM Ops Project

## Overview
The **LLM Ops Project** provides a modular and scalable framework for managing large language models (LLMs) and their associated workflows. It is designed for ease of integration with tools such as LangChain, Pinecone, and Kubeflow, while leveraging best practices for infrastructure, monitoring, and CI/CD.

## Features
- **Prompt Engineering**: Predefined and dynamic prompt templates for LLM workflows.
- **LangChain Integration**: Customizable chains to manage LLM tasks.
- **Pinecone Vector Database**: Store and query embeddings efficiently.
- **Kubeflow Pipelines**: Automate and monitor machine learning workflows.
- **Monitoring and Observability**: LangSmith and AWS CloudWatch integration.
- **Infrastructure as Code**: Terraform scripts for reproducible deployments.

## Project Structure
```plaintext
llm_ops_project/

├── Dockerfile
├── config
│   ├── __init__.py
│   ├── aws_secrets.yaml
│   ├── langchain_config.yaml
│   ├── logging_config.yaml
│   └── model_config.yaml
├── data
│   ├── cache
│   ├── embeddings
│   ├── outputs
│   └── prompts
├── examples
│   ├── kubeflow_pipeline.py
│   ├── pinecone_index.py
│   ├── simple_chain.py
│   └── step_function_handler_example.py
├── infra
│   ├── docker
│   │   └── Dockerfile
│   ├── kubeflow
│   └── terraform
│       └── secrets_manager.tf
├── monitoring
│   ├── aws_cloudwatch.py
│   ├── langsmith
│   └── prometheus_config.yaml
├── notebooks
│   ├── embeddings_analysis.ipynb
│   ├── langchain_testing.ipynb
│   └── pipeline_experiments.ipynb
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── base
│   │   ├── __init__.py
│   │   ├── kubeflow_client.py
│   │   ├── llm_client.py
│   │   └── pinecone_handler.py
│   ├── handlers
│   │   ├── __init__.py
│   │   ├── error_handler.py
│   │   └── step_function_handler.py
│   ├── prompt_engineering
│   │   ├── __init__.py
│   │   ├── chain_builder.py
│   │   ├── dynamic_prompts.py
│   │   └── templates.py
│   └── utils
│       ├── __init__.py
│       ├── logger.py
│       ├── rate_limiter.py
│       └── token_counter.py
└── tests
    ├── integration
    │   └── test_step_function_handler.py
    └── unit
```

## Getting Started

### Prerequisites
- Python 3.8 or later
- Docker
- AWS CLI (configured)
- Terraform

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/llm_ops_project.git
    cd llm_ops_project
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure environment variables (e.g., AWS credentials).

### Run Examples
- To test LangChain workflows:
    ```bash
    python examples/simple_chain.py
    ```
- To create and query a Pinecone index:
    ```bash
    python examples/pinecone_index.py
    ```
- To run a Kubeflow pipeline:
    ```bash
    python examples/kubeflow_pipeline.py

- To test Step Function integrations:
    ```bash
    python examples/step_function_handler_example.py
    ```

    ```

## Development
### Directory Structure
- **`src/`**: Contains the core modules for LLM integrations, prompt engineering, and utilities.
- **`config/`**: Holds YAML files for configuring models, logging, and AWS credentials.

### Testing
Run unit and integration tests:
```bash
pytest tests/
```
- To run integration tests:
    ```bash
    pytest tests/integration/
    ```
- To test Jupyter notebooks:
    ```bash
    pytest --nbval notebooks/
    ```

### CI/CD
- GitHub Actions workflows are set up for:
  - Linting and testing (`.github/workflows/lint_and_test.yml`).
  - Deployment to AWS (`.github/workflows/deploy.yml`).

## Infrastructure
- **Terraform**: Scripts for deploying required AWS resources (e.g., S3 buckets, Lambda functions).
- **Docker**: Containerize workflows for reproducibility.
- **Kubeflow**: Manage pipelines for training and deployment.

## Monitoring
- **LangSmith**: Observability for LangChain workflows.
- **AWS CloudWatch**: Logs and metrics for infrastructure.
- **Prometheus**: Monitoring for Kubeflow.

## Components
- **AWS CloudWatch:** Logs and metrics for the AWS ecosystem.
- **LangSmith:** Monitoring for LangChain-based workflows.
- **Prometheus:** Metrics scraping and alerting.
- **Grafana:** Visualization for Prometheus metrics.

## How to Use
1. Configure AWS credentials and run `aws_cloudwatch.py` to push metrics.
2. Use LangSmith client scripts to track LangChain performance.
3. Start Prometheus with `prometheus_config.yaml` and visualize in Grafana using `grafana_dashboard.json`.

## Future Enhancements
- Add OpenTelemetry for distributed tracing.
- Include alerts for key performance metrics.


## Contributing
1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature/new_feature
    ```
3. Commit changes and open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or feedback, reach out to [David Stroud](mailto:david@davidstroud.me).

