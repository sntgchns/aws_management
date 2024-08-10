import boto3, pprint

client = boto3.client('lambda')

# list all lambda functions names
response = client.list_functions()
# print(response)

#print all lambda functions names
for function in response['Functions']:
    print(function['FunctionName'])

# # save response to json file
# with open('lambda/lambda_functions.json', 'w') as f:
#     pprint.pprint(response, f)
