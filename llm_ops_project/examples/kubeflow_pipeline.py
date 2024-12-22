from src.handlers.step_function_handler import StepFunctionHandler
from config import aws_secrets

def trigger_llm_ops_pipeline(data):
    step_function_handler = StepFunctionHandler(aws_secrets["step_function_arn"])
    response = step_function_handler.start_execution(input_payload=data)
    print(f"Pipeline triggered. Execution ARN: {response['executionArn']}")
