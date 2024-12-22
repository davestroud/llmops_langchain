from src.handlers.step_function_handler import StepFunctionHandler

def run_step_function_example():
    # Instantiate the StepFunctionHandler
    step_function = StepFunctionHandler()

    # Define a payload for the state machine
    payload = {
        "task": "LLM Ops example",
        "parameters": {"key": "value"}
    }

    # Trigger the step function and monitor
    execution_arn = step_function.trigger_state_machine(payload)
    print(f"Step Function Execution ARN: {execution_arn}")

    # Wait for completion and fetch the result
    result = step_function.get_execution_result(execution_arn)
    print("Execution Result:", result)

if __name__ == "__main__":
    run_step_function_example()
