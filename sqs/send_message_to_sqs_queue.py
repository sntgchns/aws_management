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


def send_queue_message(queue_url, msg_attributes, msg_body):
    """
    Sends a message to the specified queue.
    """
    try:
        response = sqs_client.send_message(QueueUrl=queue_url,
                                           MessageAttributes=msg_attributes,
                                           MessageBody=msg_body)
    except ClientError:
        logger.exception(f'Could not send meessage to the - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = '<your-queue-url>'
    MSG_ATTRIBUTES = {
        'Title': {
            'DataType': 'String',
            'StringValue': 'Working with SQS in Python using Boto3'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Abhinav D'
        }
    }
    MSG_BODY = 'Learn how to create, receive, delete and modify SQS queues and see the other functions available within the AWS.'

    msg = send_queue_message(QUEUE_URL, MSG_ATTRIBUTES, MSG_BODY)

    json_msg = json.dumps(msg, indent=4)

    logger.info(f'''
        Message sent to the queue {QUEUE_URL}.
        Message attributes: \n{json_msg}''')