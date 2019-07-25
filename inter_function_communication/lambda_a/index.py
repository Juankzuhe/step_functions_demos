import boto3
import json
import logging
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lambda_client = boto3.client('lambda')
sns_client = boto3.client('sns')
MESSAGE = json.dumps({'test': True})


def main(event, context):
    logger.info("Event received: {}".format(json.dumps(event)))
    # Invoke directly
    # lambda_client.invoke(
    #     FunctionName=config.get("aws", "sns_invoke"),
    #     Payload=MESSAGE
    # )

    # Invoke via sns
    sns_client.publish(
        TopicArn=config.get("aws", "lambda_b"),
        Message=MESSAGE
    )

    logger.info("Event successed: true")
    return 'Hola pass'
