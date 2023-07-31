import boto3
import json
from botocore.exceptions import ClientError

# GET: Retrieve all tasks
def handler(event: Event, context):
    response = table.scan()

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
