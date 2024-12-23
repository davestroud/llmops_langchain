resource "aws_lambda_function" "preprocess_lambda" {
  function_name = "preprocess-data"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_role.arn
  handler       = "preprocess.data.lambda_handler"
  
  source_code_hash = filebase64sha256("lambda.zip")
  filename         = "lambda.zip"

  environment {
    variables = {
      BUCKET_NAME = "your-bucket-name"
    }
  }
}
