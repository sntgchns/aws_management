import boto3

iam = boto3.client('iam')

rsp = iam.list_groups()
groups = rsp['Groups']
index = 1

for group in groups:
    print(f'{index}: {group["GroupName"]}')
    index += 1

option = int(input("Please pick a group number: "))
arn = groups[option-1]["Arn"]
print(f'You selected group {option}: {arn}')