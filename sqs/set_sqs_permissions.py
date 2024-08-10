import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-east-1'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sqs_client = boto3.client("sqs", region_name=AWS_REGION)


def add_access_permissions(queue_url, label, account_ids, actions):
    """
    Adds permission to a queue for a specific principal.
    """
    try:
        response = sqs_client.add_permission(QueueUrl=queue_url,
                                             Label=label,
                                             AWSAccountIds=account_ids,
                                             Actions=actions)
    except ClientError:
        logger.exception(f'Could not add permissions for - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    LABEL = 'sntgchnsSendMessage'
    ACCOUNT_IDS = ['979450158315']
    ACTIONS = ['SendMessage', 'DeleteMessage']

    permissions = add_access_permissions(QUEUE_URL, LABEL, ACCOUNT_IDS,
                                         ACTIONS)

    logger.info(f'Permissions added to the queue with the label {LABEL}.')