import boto3

aws_resource = boto3.resource('s3')
bucket_name = aws_resource.Bucket('sntgchns-s3-bucket')

# response = bucket.create(
#     ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'af-south-1'|'ap-east-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ca-central-1'|'cn-north-1'|'cn-northwest-1'|'EU'|'eu-central-1'|'eu-north-1'|'eu-south-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'me-south-1'|'sa-east-1'|'us-east-2'|'us-gov-east-1'|'us-gov-west-1'|'us-west-1'|'us-west-2'
#     },
#     GrantFullControl='string',
#     GrantRead='string',
#     GrantReadACP='string',
#     GrantWrite='string',
#     GrantWriteACP='string',
#     ObjectLockEnabledForBucket=True|False,
#     ObjectOwnership='BucketOwnerPreferred'|'ObjectWriter'|'BucketOwnerEnforced'
# )

response = bucket_name.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },
)

print(response)
