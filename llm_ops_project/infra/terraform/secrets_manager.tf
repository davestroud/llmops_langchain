resource "aws_secretsmanager_secret" "llm_ops_secrets" {
  name = "llm_ops_project_secrets"
}

resource "aws_secretsmanager_secret_version" "llm_ops_secrets_version" {
  secret_id = aws_secretsmanager_secret.llm_ops_secrets.id
  secret_string = jsonencode({
    "AWS_ACCESS_KEY" : var.aws_access_key,
    "AWS_SECRET_KEY" : var.aws_secret_key,
  })
}
