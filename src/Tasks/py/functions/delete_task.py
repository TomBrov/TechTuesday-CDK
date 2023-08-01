import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# DELETE: Delete a task by ID
def handler(event: Event, context):
    table.delete_item(Key={'taskId': event['taskId']})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task deleted successfully'})
    }