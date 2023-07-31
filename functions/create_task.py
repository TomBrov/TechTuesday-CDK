import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

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