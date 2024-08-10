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


def configure_queue_long_polling(queue_url, msg_rcv_wait_time):
    """
    Configure queue to for long polling.
    """
    try:
        response = sqs_client.set_queue_attributes(
            QueueUrl=queue_url,
            Attributes={'ReceiveMessageWaitTimeSeconds': msg_rcv_wait_time})
    except ClientError:
        logger.exception(f'Could not configure long polling on - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    MSG_RCV_WAIT_TIME = '20'

    queue = configure_queue_long_polling(QUEUE_URL, MSG_RCV_WAIT_TIME)

    logger.info(f'Queue {QUEUE_URL} configured for long polling.')