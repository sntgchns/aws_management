import boto3

aws_resource = boto3.client('s3')

aws_resource.delete_bucket_policy(Bucket='sntgchns-S3-Bucket')

