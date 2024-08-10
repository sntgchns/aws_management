import boto3

aws_resource = boto3.client('s3')

objects = aws_resource.list_objects(Bucket='9j6lnpa-fei0ikn')['Contents']


if len(objects) > 0:
    print(type(objects))
    print(len(objects))

# objects
print('Objects in the bucket:')
for object in objects:
    print(object)

# files
for files in objects:
    print(files['Key'])