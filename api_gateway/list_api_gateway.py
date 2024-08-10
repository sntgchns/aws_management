import boto3

client = boto3.client('apigateway')

# list all api gateway
response = client.get_rest_apis()
# print(response)

# print api gateway ids
for api in response['items']:
    print(api['id'])