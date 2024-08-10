import boto3

AWS_REGION = "us-east-1"

sqs_client = boto3.client("sqs", region_name=AWS_REGION)