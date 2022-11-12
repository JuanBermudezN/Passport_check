# What is this?
This is a Python application to check if my Venezuelan passport has arrived to the venezuelan embassy in Argentina. I often forget to check the embassy webpage, so I created this project to automate that process with AWS Lambda and Event Bridge, the infrastructure is going to be deployed with Terraform scripts.

# How this works?
When the lambda handler is triggered is going to make a request to the Venezuelan embassy wep page and scrap the status of the passport from a Javascript alert. Then, the application is going to use the free https://www.callmebot.com/ API to send whatsapp messages, if you want to consume this great API here is the documentation https://www.callmebot.com/blog/free-api-whatsapp-messages/.

# How to use it?
If you want to use this project or the terraform scripts to deploy a similar function, these are the steps I followed:

## Setup Virtual Env for the Lambda Application Code
 
You can setup the application package with the official documentation of AWS https://docs.aws.amazon.com/lambda/latest/dg/python-package.html to create a python lambda package. 

## You need to setup API keys to use the callmebot API
you can setup the keys following this article https://www.callmebot.com/blog/free-api-whatsapp-messages/

## Customize the Terraform Scripts
To customize the terraform scripts, in my case I used a variables file, that use terraform environmental variables, if you want to follow this approach you can follow this great article https://medium.com/codex/how-to-use-environment-variables-on-terraform-f2ab6f95f82d .

## You must have an AWS Account with the neccesary permissions and create ACCESS KEYS and AWS SECRET KEYS for the AWS user
If you are familiar with AWS, you only need to configure the AWS CLI with the Keys and terraform is going to use those credentials automatically.

