import boto3
import json
import os
from botocore.exceptions import ClientError
import uuid

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def check_if_exists(tasksName):
    items = table.scan()['Items']
    items = [item for item in items if item['status'] != 'COMPLETE']
    task_names = [task['taskName'] for task in items]
    if tasksName in task_names:
        return True
    else:
        return False


# POST: Create Task
def handler(event, context):
    body = json.loads(event['body'])
    id = str(uuid.uuid4())
    item = {
        'id': id,
        'taskName': body['taskName'],
        'dueDate': body['dueDate'],
        'description': body['description'],
        'status': 'INCOMPLETE'
    }

    if check_if_exists(body['taskName']):
        return {
            'statusCode': 400,
            'body': json.dumps({"message": f"Task with Name {body['taskName']} already exists"})
        }
    else:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
