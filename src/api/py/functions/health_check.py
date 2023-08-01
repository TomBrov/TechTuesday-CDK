import boto3
import json
import os


# health check
def handler(event: Event, context):
    return {
        "Message": "Hello from Lambda!"
    }
