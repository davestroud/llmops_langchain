import pinecone
from langchain.vectorstores import Pinecone

# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key", environment="us-east-1-aws")

# Create an index
index_name = "llm-ops-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=512)

# Connect to the index
index = pinecone.Index(index_name)

# Add vectors
vectors = [
    ("id1", [0.1, 0.2, 0.3]),
    ("id2", [0.4, 0.5, 0.6]),
]
index.upsert(vectors)

# Query the index
query_vector = [0.2, 0.1, 0.3]
results = index.query(query_vector, top_k=2, include_metadata=True)
print("Query results:", results)
