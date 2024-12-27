provider "yaml" {}

data "yaml_decode" "aws_secrets" {
  input = file("${path.module}/../../config/aws_secrets.yaml")
}

resource "aws_secretsmanager_secret_version" "llm_ops_secrets_version" {
  secret_id = aws_secretsmanager_secret.llm_ops_secrets.id
  secret_string = jsonencode({
    "AWS_ACCESS_KEY" : data.yaml_decode.aws_secrets.content["aws_access_key"],
    "AWS_SECRET_KEY" : data.yaml_decode.aws_secrets.content["aws_secret_key"],
  })
}