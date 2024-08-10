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


def configure_queue_attributes(queue_url, delay_seconds, max_msg_size):
    """
    Configure queue attributes.
    """
    try:
        response = sqs_client.set_queue_attributes(QueueUrl=queue_url,
                                                   Attributes={
                                                       'DelaySeconds':
                                                       delay_seconds,
                                                       'MaximumMessageSize':
                                                       max_msg_size
                                                   })
    except ClientError:
        logger.exception(f'Could not set attributes on - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    DELAY_SECONDS = '15'
    MAX_MSG_SZIE = '2048'

    queue = configure_queue_attributes(QUEUE_URL, DELAY_SECONDS, MAX_MSG_SZIE)

    logger.info(f'Queue {QUEUE_URL} attributes created.')