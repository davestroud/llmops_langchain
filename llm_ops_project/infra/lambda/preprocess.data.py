import boto3

def lambda_handler(event, context):
    # Assume input data is in S3
    input_bucket = event['input_bucket']
    input_key = event['input_key']
    output_bucket = event['output_bucket']
    output_key = "preprocessed_" + input_key

    s3 = boto3.client('s3')
    # Fetch and preprocess data
    data = s3.get_object(Bucket=input_bucket, Key=input_key)["Body"].read()
    preprocessed_data = data.decode("utf-8").upper()  # Example preprocessing

    # Store preprocessed data back to S3
    s3.put_object(Bucket=output_bucket, Key=output_key, Body=preprocessed_data)
    
    return {
        "status": "SUCCESS",
        "output_key": output_key,
        "output_bucket": output_bucket
    }
