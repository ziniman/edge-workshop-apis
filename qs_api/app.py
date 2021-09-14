import json
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Event Data: ' + json.dumps(event))

    ip = event['requestContext']['http']['sourceIp']
    qs = event['queryStringParameters']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "ok",
            "location": ip,
            "queryString": qs
        }),
    }
