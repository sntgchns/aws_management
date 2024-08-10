import boto3

aws_resource = boto3.client('s3')

policy = aws_resource.get_bucket_policy(Bucket='9j6lnpa-fei0ikn')['Policy']

print(policy)