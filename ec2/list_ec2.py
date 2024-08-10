from http import client
import boto3

client = boto3.client('ec2')

# list all ec2 instances ids
response = client.describe_instances()
# print(response)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])