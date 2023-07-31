import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# POST: Create Task
def handler(event: Event, context):
    item = {
        'taskId': event['taskId'],
        'taskName': event['taskName'],
        'dueDate': event['dueDate'],
        'description': event['description'],
        'status': 'INCOMPLETE'
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }