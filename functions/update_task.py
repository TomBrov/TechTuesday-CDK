import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

# PUT: Update a task by ID
def handler(event: Event, context):
    table.update_item(
        Key={
            'taskId': event['taskId'],
        },
        UpdateExpression='set taskName=:n, dueDate=:d, description=:desc',
        ExpressionAttributeValues={
            ':n': event['taskName'],
            ':d': event['dueDate'],
            ':desc': event['description']
        },
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

