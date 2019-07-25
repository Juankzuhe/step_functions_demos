import json
import boto3
import configparser


config = configparser.ConfigParser()
config.read("config.ini")


def main(event, context):
    event = event.get('details')
    message = {
        "message": "Welcome {} {}".format(event['first_name'],
                                          event['last_name'])}
    client = boto3.client("sns")
    client.publish(
        TargetArn=config.get("aws", "sns"),
        Message=json.dumps(
            {'default': json.dumps(message.get("message", ""))}),
        MessageStructure='json'
    )

    return message.get("message", "")
