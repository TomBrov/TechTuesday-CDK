import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

# DELETE: Delete a task by ID
def handler(event: Event, context):
    table.delete_item(Key={'taskId': event['taskId']})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task deleted successfully'})
    }