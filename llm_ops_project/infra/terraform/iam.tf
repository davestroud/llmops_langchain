resource "aws_iam_role" "step_functions_role" {
  name = "StepFunctionsExecutionRole"
  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "states.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "step_functions_policy" {
  name = "StepFunctionsPolicy"
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "lambda:InvokeFunction",
          "sagemaker:CreateTrainingJob", # TODO: change to the actual action
          "sagemaker:CreateEndpoint", # TODO: change to the actual action
          "sagemaker:DescribeEndpoint" # TODO: change to the actual action
        ],
        "Resource": "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "step_functions_policy_attach" {
  role       = aws_iam_role.step_functions_role.name
  policy_arn = aws_iam_policy.step_functions_policy.arn
}
