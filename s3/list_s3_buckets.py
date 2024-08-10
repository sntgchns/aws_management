import boto3

aws_resource = boto3.resource('s3')
buckets = list(aws_resource.buckets.all())
print(buckets)

for bucket in buckets:
    print(bucket.name)

print('There are {} buckets'.format(len(buckets)))