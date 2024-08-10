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


def list_dead_letter_source_queues(queue_url):
    """
    Get a list of queues that have the RedrivePolicy queue attribute configured with a dead-letter queue
    """
    try:
        paginator = sqs_client.get_paginator('list_dead_letter_source_queues')

        # creating a PageIterator from the paginator
        page_iterator = paginator.paginate(
            QueueUrl=queue_url).build_full_result()

        queues = []

        # loop through each page from page_iterator
        for page in page_iterator['queueUrls']:
            queues.append(page)

    except ClientError:
        logger.exception(f'Could not get source queues for - {queue_url}.')
        raise
    else:
        return queues


if __name__ == '__main__':
    # CONSTANTS
    DLQ_URL = '<dead-letter-queue-url>'

    queues = list_dead_letter_source_queues(DLQ_URL)

    logger.info('Dead letter source queues are: ')

    for queue in queues:
        logger.info(f'Queue URL - {queue}')