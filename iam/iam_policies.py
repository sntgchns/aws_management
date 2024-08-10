import boto3

iam = boto3.client('iam')

rsp = iam.list_policies(Scope='Local', OnlyAttached=False)
policies = rsp['Policies']
index = 1

for policy in policies:
    print("%d: %s" % (index, policy["PolicyName"]))
    index += 1

option = int(input("Please pick a policy number: "))
arn = policies[option-1]["Arn"]
print("You selected policy %d: %s" % (option, arn))