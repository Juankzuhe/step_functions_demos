import json
import logging

import boto3
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main(event, context):
    logger.info("Event received: {}".format(json.dumps(event)))
    if 'email' not in event:
        logger.error("Validation Failed")
        raise Exception("Couldn't create the record: email must be present.")

    table = dynamodb.Table('Users')

    item = {key: event[key] for key in ['id', 'email', 'first_name', 'last_name']}

    table.put_item(Item=item)

    return {
        "status": 200,
        "details": item
    }
