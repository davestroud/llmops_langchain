resource "aws_sfn_state_machine" "llm_ops_pipeline" {
  name     = "LLMOpsPipeline"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = jsonencode({
    "Comment": "LLM Ops pipeline",
    "StartAt": "DataPreprocessing",
    "States": {
      "DataPreprocessing": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:region:account-id:function:preprocess-data",
        "Next": "ModelTraining"
      },
      "ModelTraining": {
        "Type": "Task",
        "Resource": "arn:aws:sagemaker:region:account-id:training-job",
        "Next": "ModelDeployment"
      },
      "ModelDeployment": {
        "Type": "Task",
        "Resource": "arn:aws:sagemaker:region:account-id:endpoint",
        "End": true
      }
    }
  })
}
