import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

# PATCH: Mark a task as complete
def handler(event: Event, context):
    table.update_item(
        Key={
            'taskId': event['taskId'],
        },
        UpdateExpression='set status=:s',
        ExpressionAttributeValues={
            ':s': 'COMPLETE'
        },
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task status updated to COMPLETE'})
    }
