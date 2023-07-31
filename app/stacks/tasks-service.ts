import * as pylambda from "@aws-cdk/aws-lambda-python-alpha";
import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import { Construct } from "constructs";

export class TasksStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props: ImageClassificationStackProps) {
        super(scope, id, props);

        // Stack tags
        cdk.Tags.of(this).add("App", "TasksService");

        const TasksTable = new dynamodb.Table(this, "TasksTable", {
          partitionKey: { name: "id", type: dynamodb.AttributeType.STRING },
          billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
          cdk.RemovalPolicy.DESTROY,
        });

        const CreateTaskFn = new pylambda.PythonFunction(this, "CreateTaskFn", {
          entry: "src/py",
          index: "Tasks/create_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadWriteData(CreateTaskFn);

        const GetTaskFn = new pylambda.PythonFunction(this, "GetTaskFn", {
          entry: "src/py",
          index: "Tasks/get_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadData(GetTaskFn);

        const GetTasksFn = new pylambda.PythonFunction(this, "GetTasksFn", {
          entry: "src/py",
          index: "Tasks/get_tasks.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadData(GetTasksFn);

        const UpdateTaskFn = new pylambda.PythonFunction(this, "UpdateTaskFn", {
          entry: "src/py",
          index: "Tasks/update_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadWriteData(UpdateTaskFn);

        const DeleteTaskFn = new pylambda.PythonFunction(this, "DeleteTaskFn", {
          entry: "src/py",
          index: "Tasks/delete_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadWriteData(DeleteTaskFn);

        const CompleteTaskFn = new pylambda.PythonFunction(this, "CompleteTaskFn", {
          entry: "src/py",
          index: "Tasks/complete_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: TasksTable.tableName,
          },
        });
        TasksTable.grantReadWriteData(CompleteTaskFn);
}