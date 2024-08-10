import boto3

# Upload single file
aws_resource = boto3.client('s3')
aws_resource.upload_file(
    Filename='sntgchns_uploaded.png',
    Bucket='sntgchns-s3-bucket',
    Key='sntgchns.png',
    # ExtraArgs=None,
    # Callback=None,
    # Config=None,
)

# Upload multiple files
import os
import glob

cwd = os.getcwd()
cwd = cwd + '/upload/'
files = glob.glob(cwd + '*.png')

print(files)

for file in files:    
    aws_resource = boto3.client('s3')
    aws_resource.upload_file(
        Filename=file,
        Bucket='sntgchns-s3-bucket',
        Key=file.split('/')[-1],
        # ExtraArgs=None,
        # Callback=None,
        # Config=None,
    )