import boto3
import json

# Initialize AWS Step Functions client
client = boto3.client("stepfunctions", region_name="us-west-2")

# Define the state machine ARN and input
state_machine_arn = "arn:aws:states:us-west-2:123456789012:stateMachine:MyStateMachine"
input_payload = {
    "task": "process_data",
    "params": {"data_location": "s3://my-bucket/input-data/"}
}

# Start the execution
response = client.start_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps(input_payload)
)

print("Execution ARN:", response["executionArn"])
