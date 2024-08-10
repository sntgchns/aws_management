import boto3, pprint

client = boto3.client('cloudfront')

# list all cloudfront
response = client.list_distributions()
# print(response)

# print all cloudfront arn
for item in response['DistributionList']['Items']:
    print(item['ARN'])

# # save response to json file
# with open('cloudfront/cloudfront_list.json', 'w') as f:
#     pprint.pprint(response, f)