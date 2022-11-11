resource "aws_lambda_function" "check_document" {
    filename = "../app.zip"
    function_name = "check_document"
    handler = "main.lambda_handler"
    runtime = "python3.8"
    timeout = 60
    role = aws_iam_role.iam_for_lambda.arn
    tags = {
        NAME = "CHECK_DOCUMENT"
        ENV = "DEVELOPMENT"
    }
    environment {
        variables = {
            URL_EMBAJADA = var.URL_EMBAJADA
            CEDULA_IDENTIDAD = var.CEDULA_IDENTIDAD
            WSP_API_URL = var.WSP_API_URL
            PHONE_NUMBER = var.PHONE_NUMBER
            WSP_API_KEY = var.WSP_API_KEY
        }
    }
}

data "aws_iam_policy_document" "policy" {
  statement {
    sid    = ""
    effect = "Allow"
    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.policy.json
  }