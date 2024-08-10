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


def purge_queue(queue_url):
    """
    Deletes the messages in a specified queue
    """
    try:
        response = sqs_client.purge_queue(QueueUrl=queue_url)

    except ClientError:
        logger.exception(f'Could not purge the queue - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'

    purge = purge_queue(QUEUE_URL)

    logger.info(f'All the message from {QUEUE_URL} are purged.')