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


def receive_queue_message(queue_url):
    """
    Retrieves one or more messages (up to 10), from the specified queue.
    """
    try:
        response = sqs_client.receive_message(QueueUrl=queue_url)
    except ClientError:
        logger.exception(
            f'Could not receive the message from the - {queue_url}.')
        raise
    else:
        return response


def delete_queue_message(queue_url, receipt_handle):
    """
    Deletes the specified message from the specified queue.
    """
    try:
        response = sqs_client.delete_message(QueueUrl=queue_url,
                                             ReceiptHandle=receipt_handle)
    except ClientError:
        logger.exception(
            f'Could not delete the meessage from the - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'

    messages = receive_queue_message(QUEUE_URL)

    for msg in messages['Messages']:
        msg_body = msg['Body']
        receipt_handle = msg['ReceiptHandle']

        logger.info(f'The message body: {msg_body}')

        logger.info('Deleting message from the queue...')

        delete_queue_message(QUEUE_URL, receipt_handle)

    logger.info(f'Received and deleted message(s) from {QUEUE_URL}.')