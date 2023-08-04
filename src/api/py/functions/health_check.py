import boto3
import json
import os


# health check
def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            "Message": "Hello from Lambda!"
        }),
        "isBase64Encoded": False
    }