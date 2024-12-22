import pytest
from src.handlers.step_function_handler import StepFunctionHandler

@pytest.fixture
def step_function_handler():
    return StepFunctionHandler()

def test_step_function_execution(step_function_handler):
    payload = {"task": "Test Task", "parameters": {"test": "value"}}
    
    execution_arn = step_function_handler.trigger_state_machine(payload)
    assert execution_arn.startswith("arn:aws:states"), "Invalid ARN format"

    result = step_function_handler.get_execution_result(execution_arn)
    assert "status" in result, "Execution result missing 'status'"
