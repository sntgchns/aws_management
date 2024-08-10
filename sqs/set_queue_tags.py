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


def apply_queue_tags(queue_url, tags):
    """
    Add resource tags to the specified Amazon SQS queue.
    """
    try:
        response = sqs_client.tag_queue(QueueUrl=queue_url, Tags=tags)
    except ClientError:
        logger.exception(f'Could not set tags on - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    TAGS = {
        'Name': 'name-of-standard-queue',
        'Team': 'name-of-team',
        'Type': 'standard'
    }

    queue = apply_queue_tags(QUEUE_URL, TAGS)

    logger.info(f'Resource tags applied to the queue - {QUEUE_URL}.')