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


def list_queues():
    """
    Creates an iterable of all Queue resources in the collection.
    """
    try:
        sqs_queues = []
        for queue in sqs_resource.queues.all():
            sqs_queues.append(queue)
    except ClientError:
        logger.exception('Could not list queues.')
        raise
    else:
        return sqs_queues


if __name__ == '__main__':
    lst_of_sqs_queues = list_queues()

    for queue in lst_of_sqs_queues:
        logger.info(f'Queue URL - {queue.url}')