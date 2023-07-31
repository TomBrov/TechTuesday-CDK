import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

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

