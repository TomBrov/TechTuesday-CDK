import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# GET: Retrieve a task by ID
def handler(event, context):
    path = event["path"]
    task_id = path.split("/")[-1]

    try:
        response = table.get_item(Key={'id': task_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
