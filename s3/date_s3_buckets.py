import boto3

aws_resource = boto3.client('s3')

creation_date = aws_resource.list_buckets()['Buckets'][4]['CreationDate']
print(creation_date.strftime('%Y-%m-%d %H:%M:%S+00:00'))

for bucket in aws_resource.list_buckets()['Buckets']:
    print('Bucket name: {}'.format(bucket['Name']))
    print('Created at: {}'.format(bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S+00:00')))
