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


def get_queue(queue_name):
    """
    Returns the URL of an existing Amazon SQS queue.
    """
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)['QueueUrl']

    except ClientError:
        logger.exception(f'Could not get the {queue_name} queue.')
        raise
    else:
        return response


if __name__ == '__main__':

    # Constants
    QUEUE_NAME = 'name of the queue whose URL is to be retrieved e.g.: (name-of-standard-queue)'
    queue = get_queue(QUEUE_NAME)
    logger.info(f'Queue URL - {queue}')