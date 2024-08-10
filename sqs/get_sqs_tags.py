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


def get_queue_tags(queue_url):
    """
    List all resource tags added to the specified Amazon SQS queue.
    """
    try:
        response = sqs_client.list_queue_tags(QueueUrl=queue_url)
    except ClientError:
        logger.exception(f'Could not get tags for - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'

    tags = get_queue_tags(QUEUE_URL)

    logger.info('Tags for the queue: ')

    for key, value in tags['Tags'].items():
        print(f'Tag Key: {key}, Tag Value: {value}')