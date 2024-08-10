import boto3
from datetime import datetime, timedelta

client = boto3.client('iam')
users = client.list_users()

flaggedUsers = []
flaggedUserThreshold = 90 # days since last activity

for key in users['Users']:
        flaggedUser = {}
        username = key['UserName']
        
        # List access keys through the pagination interface.
        paginator = client.get_paginator('list_access_keys')

        for response in paginator.paginate(UserName=username):
                accessKeyMetadata = response['AccessKeyMetadata']
                
                # Check if user has some keys, if not continue with next user in the list 
                if len(accessKeyMetadata) != 0:
                        accessKeyId = accessKeyMetadata[0]['AccessKeyId']
                        accessKeyLastUsedResponse = client.get_access_key_last_used(AccessKeyId=accessKeyId)
                        accessKeyLastUsed = accessKeyLastUsedResponse['AccessKeyLastUsed']
                        lastUsedDate = accessKeyLastUsed['LastUsedDate']
                        lastActivity = datetime.now(lastUsedDate.tzinfo) - lastUsedDate

                        accessKeyCreationDate = accessKeyMetadata[0]['CreateDate']
                        accessKeyAge = datetime.now(accessKeyCreationDate.tzinfo) - accessKeyCreationDate

                        if lastActivity.days >= flaggedUserThreshold or accessKeyAge.days >= flaggedUserThreshold:
                                flaggedUser['username'] = key['UserName']
                                flaggedUser['accessKeyId'] = accessKeyId
                                flaggedUser['lastActivity'] = lastActivity.days
                                flaggedUser['accessKeyAge'] = accessKeyAge.days
                                flaggedUsers.append(flaggedUser)

                else:
                        continue

# Print all the flagged users
print(flaggedUsers)