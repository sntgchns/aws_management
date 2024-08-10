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


def create_queue(queue_name, delay_seconds, visiblity_timeout):
    """
    Create a standard SQS queue
    """
    try:
        response = sqs_resource.create_queue(QueueName=queue_name,
                                             Attributes={
                                                 'DelaySeconds': delay_seconds,
                                                 'VisibilityTimeout': visiblity_timeout
                                             })
    except ClientError:
        logger.exception(f'Could not create SQS queue - {queue_name}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_NAME = 'name-of-standard-queue'
    DELAY_SECONDS = '0'
    VISIBLITY_TIMEOUT = '60'

    output = create_queue(QUEUE_NAME, DELAY_SECONDS, VISIBLITY_TIMEOUT)

    logger.info(
        f'Standard Queue {QUEUE_NAME} created. Queue URL - {output.url}')