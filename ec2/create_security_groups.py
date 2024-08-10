import boto3

aws_resource = boto3.client('ec2')
aws_resource.create_security_group(Description='Security group for sntgchns EC2 instances', GroupName='ec2_sntgchns_sg')

# associate the security group with the VPC
aws_resource.create_security_group(Description='Security group for sntgchns EC2 instances associated to a vpc', GroupName='ec2_sntgchns_sg_vpc', VpcId='vpc-0f128f65')