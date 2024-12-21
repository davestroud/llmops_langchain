from setuptools import setup, find_packages

setup(
    name="llm_ops_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.200",
        "openai>=0.27.0",
        "pinecone-client>=2.2.1",
        "pyyaml>=6.0",
        "python-dotenv>=0.19.0",
        "asyncio>=3.4.3",
    ],
    author="David Stroud",
    author_email="david@davidstroud.com",
    description="A LangChain-based LLM operations project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
) 