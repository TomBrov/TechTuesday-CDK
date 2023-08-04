from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import SimpleStorageServiceS3 as s3
from diagrams.aws.general import Users

with Diagram("Task Management API", show=False, filename="diagram"):
    user = Users("User Requests")

    with Cluster("AWS Region"):
        api_gateway = APIGateway("API Gateway")

        with Cluster("Lambda Functions"):
            create_task = Lambda("createTaskFn")
            get_task = Lambda("getTaskFn")
            get_tasks = Lambda("getTasksFn")
            update_task = Lambda("updateTaskFn")
            delete_task = Lambda("deleteTaskFn")
            complete_task = Lambda("completeTaskFn")
            docs = Lambda("DocsFn")

        with Cluster("DynamoDB"):
            tasks_db = Dynamodb("Tasks")

        open_api = s3("OpenApiSpec")

        user >> api_gateway

        api_gateway >> create_task >> tasks_db
        api_gateway >> get_task >> tasks_db
        api_gateway >> get_tasks >> tasks_db
        api_gateway >> update_task >> tasks_db
        api_gateway >> delete_task >> tasks_db
        api_gateway >> complete_task >> tasks_db
        api_gateway >> docs >> open_api
