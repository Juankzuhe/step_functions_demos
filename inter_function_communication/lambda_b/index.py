import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main(event, context):
    logger.info("Event received: {}".format(json.dumps(event)))

    logger.info("Event successed: true")
    return 'Holy'
