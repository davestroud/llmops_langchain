# src/handlers/step_function_handler.py
import boto3
import json

class StepFunctionHandler:
    def __init__(self, state_machine_arn):
        self.client = boto3.client('stepfunctions')
        self.state_machine_arn = state_machine_arn

    def start_execution(self, input_payload):
        response = self.client.start_execution(
            stateMachineArn=self.state_machine_arn,
            input=json.dumps(input_payload)
        )
        return response

    def get_execution_status(self, execution_arn):
        response = self.client.describe_execution(
            executionArn=execution_arn
        )
        return response['status']
