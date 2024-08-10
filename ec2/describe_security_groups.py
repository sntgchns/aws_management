import boto3

aws_resource = boto3.client('ec2')

security_groups = aws_resource.describe_security_groups()

print(security_groups)

count_security_groups = len(security_groups['SecurityGroups'])
print(f'There are {count_security_groups} security groups in this account')

for group in security_groups['SecurityGroups']:
    print(group["GroupId"])

# describe security groups by id
groups_by_id = aws_resource.describe_security_groups(GroupIds=['sg-0d2fbbdf724366fef', 'sg-015f4d0353cceba59'])
print(groups_by_id)

# describe security groups with filters
# groups_by_filters = aws_resource.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': ['default']}])
groups_by_filters = aws_resource.describe_security_groups(Filters=[{'Name': 'group-id', 'Values': ['sg-0d2fbbdf724366fef', 'sg-015f4d0353cceba59']}])
print(groups_by_filters)