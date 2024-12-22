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
│
├── config/                 # Configuration files (models, logging, AWS settings)
├── src/                    # Source code for the project
│   ├── base/               # Core components (LLM client, Pinecone handler)
│   ├── prompt_engineering/ # Prompt templates and LangChain chains
│   ├── utils/              # Utility modules (logging, token counting)
│   ├── handlers/           # Error handling
├── data/                   # Data storage (prompts, embeddings, outputs)
├── examples/               # Usage examples (LangChain, Pinecone, Kubeflow)
├── notebooks/              # Jupyter notebooks for experimentation
├── infra/                  # Infrastructure code (Terraform, Docker, Kubeflow)
├── monitoring/             # Observability configurations (LangSmith, Prometheus)
├── tests/                  # Unit and integration tests
├── .github/                # CI/CD workflows (GitHub Actions)
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
├── Dockerfile              # Docker setup
├── setup.py                # Python package setup
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

