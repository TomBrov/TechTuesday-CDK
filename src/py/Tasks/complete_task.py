import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

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
