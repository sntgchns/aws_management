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


def remove_access_permissions(queue_url, label):
    """
    Revokes any permissions in the queue policy.
    """
    try:
        response = sqs_client.remove_permission(QueueUrl=queue_url,
                                                Label=label)
    except ClientError:
        logger.exception(f'Could not remove permissions for - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    LABEL = 'sntgchnsSendMessage'

    permissions = remove_access_permissions(QUEUE_URL, LABEL)

    logger.info(f'Permissions {LABEL} removed from the queue.')