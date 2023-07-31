import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

# GET: Retrieve a task by ID
def handler(event: Event, context):
    try:
        response = table.get_item(Key={'taskId': event['taskId']})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
