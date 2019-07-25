import json
import boto3
import inflect


def lambda_handler(event, context):
    inflect_engine = inflect.engine()
    number = inflect_engine.number_to_words(event.get('final_number'))
    message = {
        "message": "Result is %r %s" % (number, event.get('final_number'))}
    client = boto3.client('sns')
    client.publish(
        TargetArn="arn:aws:sns:us-east-1:237385584587:sms_message",
        Message=json.dumps({'default': json.dumps(message.get("message", ""))}),
        MessageStructure='json'
    )

    return message.get("message", "")
