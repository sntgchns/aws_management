import boto3

aws_resource = boto3.client('s3')

# Delete single object
aws_resource.delete_object(Bucket='sntgchns-s3-bucket', Key='sntgchns_uploaded.png')

# Delete multiple objects
import os
import glob

# get all files from the bucket
objects = aws_resource.list_objects(Bucket='sntgchns-s3-bucket')['Contents']
print(len(objects))

# iterate over the files and delete them
for object in objects:
    response = aws_resource.delete_object(Bucket='sntgchns-s3-bucket', Key=object['Key'])
    print(response)
