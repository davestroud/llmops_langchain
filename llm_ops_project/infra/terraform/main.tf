module "lambda" {
  source = "./modules/lambda"
  # Pass any necessary variables
}

module "step_functions" {
  source = "./modules/step_functions"
  # Pass any necessary variables
}

module "secrets_manager" {
  source = "./modules/secrets_manager"
  # Pass any necessary variables
} 