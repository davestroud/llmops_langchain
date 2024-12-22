def monitor_step_function_execution(execution_arn):
    handler = StepFunctionHandler(state_machine_arn=aws_secrets["step_function_arn"])
    status = handler.get_execution_status(execution_arn)
    print(f"Execution Status: {status}")
