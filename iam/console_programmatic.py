import boto3

iamclient = boto3.client('iam')
iamusers = iamclient.list_users()

# Users with console access
def consoleUsers():
    consoleUsers = []
    for user in iamusers['Users']:
        try:
            if user['PasswordLastUsed']:
                consoleUsers.append(user['UserName'])
        except KeyError:
            pass
    print('List of users with console access: {}'.format(consoleUsers))
    return consoleUsers

# Users with programmatic access
def programmaticUsers():
    programmaticUsers = []
    paginator = iamclient.get_paginator('list_access_keys')
    for user in iamusers['Users']:
        for response in paginator.paginate(UserName=user['UserName']):
            for key in response['AccessKeyMetadata']:
                if key['Status'] == 'Active':
                    programmaticUsers.append(user['UserName'])
    print('List of users with programmatic access: {}'.format(programmaticUsers))
    return programmaticUsers

# Users with both console and programmatic access
def consoleProgrammatic(consoleUsers, programmaticUsers):
    consoleProgrammatic = set(consoleUsers).intersection(programmaticUsers)
    print('List of users with both console and programmatic access: {}'.format(list(consoleProgrammatic)))
    return consoleProgrammatic

#print
consoleProgrammatic(consoleUsers(), programmaticUsers())