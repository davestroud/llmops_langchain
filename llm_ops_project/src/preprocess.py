"""
Preprocessing Steps for Video Comments

1. Extract Comment Text:
   - Focus on extracting the content of the comments from the dataset.

2. Clean the Text:
   - Remove special characters, URLs, and extra whitespace.
   - Normalize text by converting it to lowercase.

3. Concatenate Comments for Each Video:
   - Combine all comments related to a single video into a single text blob.
   - This is useful for tasks such as embeddings or summarization.

4. Output Preprocessed Comments:
   - Return a DataFrame that is ready for ingestion by a Language Model (LLM).
"""

import boto3
import pyarrow as pa
from io import BytesIO
import pandas as pd
import json
import re

# Set pandas to display all rows and columns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Define the S3 bucket and file key
S3_BUCKET = "ishtar-ai"
S3_KEY = "data/raw/data-00000-of-00001.arrow"

# Initialize boto3 client
s3 = boto3.client("s3")


def load_arrow_data_from_s3(bucket, key):
    """
    Load Arrow data from S3 and convert it to a Pandas DataFrame.
    """
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


def clean_comment_text(comment_text):
    """
    Clean individual comment text for LLM ingestion.
    """
    # Remove special characters, URLs, and extra whitespace
    comment_text = re.sub(r"http\S+", "", comment_text)  # Remove URLs
    comment_text = re.sub(
        r"[^a-zA-Z0-9\s.,!?]", "", comment_text
    )  # Remove special characters
    comment_text = re.sub(r"\s+", " ", comment_text).strip()  # Remove extra whitespace
    return comment_text.lower()  # Convert to lowercase


def preprocess_comments_column(df):
    """
    Preprocess the 'comments' column, extract and clean 'comment_text',
    and concatenate all comments for each video.
    """
    if "comments" not in df.columns:
        print("No 'comments' column found.")
        return None

    def extract_comment_text(comments):
        """
        Extract and clean 'comment_text' from the comments JSON-like field.
        """
        if isinstance(comments, str):  # If comments is a string, try to parse it
            try:
                comments = json.loads(comments)
            except json.JSONDecodeError:
                return []  # Return empty list if parsing fails
        elif isinstance(comments, list):  # If comments is already a list, use it as is
            pass
        else:
            return []  # Return empty list if comments is neither a string nor a list

        # Extract comment_text and clean it
        return [
            clean_comment_text(comment.get("comment_text", "")) for comment in comments
        ]

    # Parse the comments column and extract clean text
    df["comments_parsed"] = df["comments"].apply(extract_comment_text)

    # Concatenate comments for each video into a single text blob
    df["comments_blob"] = df["comments_parsed"].apply(lambda x: " ".join(x))
    return df[["id", "title", "comments_blob"]]


# Main script execution
if __name__ == "__main__":
    # Load data from S3
    arrow_data = load_arrow_data_from_s3(S3_BUCKET, S3_KEY)

    if arrow_data:
        # Convert Arrow data to Pandas DataFrame
        df = arrow_data.to_pandas()

        # Preprocess the comments column
        preprocessed_df = preprocess_comments_column(df)

        # Display the resulting DataFrame
        print("Preprocessed DataFrame (first 5 rows):")
        print(preprocessed_df.head(5))
