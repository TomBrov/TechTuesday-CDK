import boto3
import json
import os
from botocore.exceptions import ClientError

# health check
def handler(event: Event, context):

    return {
        "Message": "Hello from Lambda!"
    }
