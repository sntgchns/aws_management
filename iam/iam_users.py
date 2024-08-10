import boto3
import pprint

iamclient = boto3.client('iam')
iamusers = iamclient.list_users()

# pprint.pprint(iamusers['Users'][11])
print(iamclient.get_user(UserName='santiago'))

# # list users and their creation date
# for userdata in iamusers['Users']:
#     username = userdata['UserName']
#     user_created = userdata['CreateDate']
#     print(f'{username}\t{user_created}')

# # for iamuser in iamusers:      
# #     if iamuser.password_last_used:
# #         print('User has console access')
# #     else:
# #         print('User has only programmatic access')

# for user in iamclient.list_users()['Users']:
#     print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
#     user['UserName'],
#     user['UserId'],
#     user['Arn'],
#     user['CreateDate']))

# paginator = iamclient.get_paginator('list_users')
# for page in paginator.paginate():
#     for user in page['Users']:
#         print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
#         user['UserName'],
#         user['UserId'],
#         user['Arn'],
#         user['CreateDate']))

# for user_detail in iamclient.get_account_authorization_details(Filter=['User'])['UserDetailList']:
#     policyname = []
#     policyarn = []
#     # find each policy attached to the user
#     for policy in user_detail['AttachedManagedPolicies']:
#         policyname.append(policy['PolicyName'])
#         policyarn.append(policy['PolicyArn'])
#         # print user details 
#         print("User: {0}\nUserID: {1}\nPolicyName: {2}\nPolicyARN: {3}\n".format(
#         user_detail['UserName'],
#         user_detail['UserId'],
#         policyname,
#         policyarn
#         )
#         )

# # create users and assign policies
# userlist = ['sntgchns_user_1', 'sntgchns_user_2', 'sntgchns_user_3']
# userPolicyList = ['arn:aws:iam::aws:policy/AmazonS3FullAccess','arn:aws:iam::aws:policy/AmazonEC2FullAccess','arn:aws:iam::aws:policy/AmazonVPCFullAccess']

# # assign index to each user
# count =len(userlist)

# for sntgchns_user_index in range(count):
#     iamclient.create_user(UserName=userlist[sntgchns_user_index].strip())
#     iamclient.attach_user_policy(UserName=userlist[sntgchns_user_index].strip(),PolicyArn=userPolicyList[sntgchns_user_index].strip())
#     print(f'{userlist[sntgchns_user_index].strip()} created and attached policies')

# # create an access key for each user
# create_keys = iamclient.create_access_key(UserName='sntgchns_user_1')
# print(create_keys)

# # delete user access keys
# delete_keys = iamclient.delete_access_key(UserName='sntgchns_user_1',AccessKeyId='AKIAIOSFODNN7EXAMPLE')

# # detach policies
# detach_policy = iamclient.detach_user_policy(UserName='sntgchns_user_1',PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')

# # delete user
# delete_user = iamclient.delete_user(UserName='sntgchns_user_1')