import boto3

AWS_REGION = "us-east-1"

sqs_resource = boto3.resource("sqs", region_name=AWS_REGION)