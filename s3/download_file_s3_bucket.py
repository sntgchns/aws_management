import boto3

aws_resource = boto3.client('s3')

# download single file from s3 bucket
aws_resource.download_file(Bucket='sntgchns-s3-bucket', Key='sntgchns_uploaded.png', Filename='sntgchns_uploaded.png')

# download multiple files from s3 bucket
import os
import glob

cwd = os.getcwd()
cwd = cwd + '/download/'

files = aws_resource.list_objects(Bucket='sntgchns-s3-bucket')['Contents']
print(len(files))
print(files)

for file in files:
    aws_resource.download_file(Bucket='sntgchns-s3-bucket', Key=file['Key'], Filename=cwd + file['Key'])