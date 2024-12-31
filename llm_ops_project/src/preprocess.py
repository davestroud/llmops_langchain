import boto3
import pyarrow as pa
import pyarrow.parquet as pq  # For handling Arrow formats
from io import BytesIO
import pandas as pd

# Set pandas to display all rows and columns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Define the S3 bucket and file key
S3_BUCKET = "ishtar-ai"
S3_KEY = "data/raw/data-00000-of-00001.arrow"

# Initialize boto3 client
s3 = boto3.client("s3")


def load_arrow_data_from_s3(bucket, key):
    try:
        # Fetch the file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read()

        # Load data using PyArrow
        arrow_table = pa.ipc.open_stream(BytesIO(file_content)).read_all()
        print("Data successfully loaded from S3!")
        return arrow_table
    except Exception as e:
        print(f"Error loading data from S3: {e}")
        return None


# Load the data
arrow_data = load_arrow_data_from_s3(S3_BUCKET, S3_KEY)

# Convert to Pandas DataFrame if needed
if arrow_data:
    df = arrow_data.to_pandas()

    # Print the entire DataFrame
    print("Full DataFrame:")
    print(df.head(5))
