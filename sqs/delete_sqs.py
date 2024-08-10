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


def delete_queue(queue_name):
    """
    Deletes the queue specified by the QueueUrl.
    """
    try:
        response = sqs_client.delete_queue(QueueUrl=queue_name)

    except ClientError:
        logger.exception(f'Could not delete the {queue_name} queue.')
        raise
    else:
        return response


if __name__ == '__main__':

    # Constants
    QUEUE_URL = '<your-queue-url>'
    queue = delete_queue(QUEUE_URL)
    logger.info(f'{QUEUE_URL} deleted successfully.')