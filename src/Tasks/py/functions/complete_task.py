import boto3
import json
import os
from botocore.exceptions import ClientError

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# PATCH: Mark a task as complete
def handler(event, context):
    path = event["path"]
    task_id = path.split("/")[-1]
    #
    # table.update_item(
    #     Key={'id': task_id},
    #     UpdateExpression='set status=:s',
    #     ExpressionAttributeValues={':s': 'COMPLETE'},
    #     ReturnValues='UPDATED_NEW'
    # )
    try:
        table.update_item(
            Key={'id': task_id},
            AttributeUpdates={'status': {'Value': 'COMPLETE', 'Action': 'PUT'}},
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to update task status'})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task status updated to COMPLETE'})
        }
