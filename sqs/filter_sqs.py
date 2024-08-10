import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-east-1'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sqs_resource = boto3.resource("sqs", region_name=AWS_REGION)


def filter_queues(queue_prefix):
    """
    Creates an iterable of filtered Queue resources in the collection.
    """
    try:
        sqs_queues = []

        filtered_queues = sqs_resource.queues.filter(
            QueueNamePrefix=queue_prefix)

        for queue in filtered_queues:
            sqs_queues.append(queue)
    except ClientError:
        logger.exception(f'Could not filter queues for prefix {queue_prefix}.')
        raise
    else:
        return sqs_queues


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_PREFIX = 'queue name prefix to use for filtering the list results'

    lst_of_sqs_queues = filter_queues(QUEUE_PREFIX)

    logger.info(f'A list of SQS queue(s) starting with prefix {QUEUE_PREFIX}:')

    for queue in lst_of_sqs_queues:
        logger.info(f'Queue URL - {queue.url}')