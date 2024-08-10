from pydoc import describe
import boto3

aws_resource = boto3.client('ec2')

# create a VPC
aws_resource.create_vpc(CidrBlock='10.0.0.0/16')

# describe VPC
describe_vpc = aws_resource.describe_vpcs()
print(describe_vpc)

# count the number of VPCs
vpcs = describe_vpc['Vpcs']
vpc_count = len(vpcs)
print(vpc_count)

# print the VPC ID
for vpc in vpcs:
    print(vpc['VpcId'])
    print(vpc['CidrBlock'])
    print(vpc['IsDefault'])

# describe VPC by ID
vpc_id = aws_resource.describe_vpcs(VpcIds=['vpc-0f128f65'])
print(vpc_id)