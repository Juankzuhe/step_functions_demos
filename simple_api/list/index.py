import json
import logging

import boto3
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main(event, context):
    logger.info("Event received: {}".format(json.dumps(event)))

    table = dynamodb.Table('Users')

    users = table.scan()

    return {
        "status": 200,
        "details": users.get('Items')
    }
