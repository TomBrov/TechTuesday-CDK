import * as pylambda from "@aws-cdk/aws-lambda-python-alpha";
import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class TasksStack extends cdk.Stack {
    public readonly createTaskFn: lambda.IFunction;
    public readonly getTaskFn: lambda.IFunction;
    public readonly getTasksFn: lambda.IFunction;
    public readonly updateTaskFn: lambda.IFunction;
    public readonly deleteTaskFn: lambda.IFunction;
    public readonly completeTaskFn: lambda.IFunction;

    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Stack tags
        cdk.Tags.of(this).add("App", "TasksService");

        const tasksTable = new dynamodb.Table(this, "tasksTable", {
          partitionKey: { name: "id", type: dynamodb.AttributeType.STRING },
          billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
        });

        this.createTaskFn = new pylambda.PythonFunction(this, "createTaskFn", {
          entry: "src/Tasks/py",
          index: "functions/create_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: tasksTable.tableName,
          },
        });
        tasksTable.grantReadWriteData(this.createTaskFn);

        this.getTaskFn = new pylambda.PythonFunction(this, "getTaskFn", {
          entry: "src/Tasks/py",
          index: "functions/get_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: tasksTable.tableName,
          },
        });
        tasksTable.grantReadData(this.getTaskFn);

        this.getTasksFn = new pylambda.PythonFunction(this, "getTasksFn", {
          entry: "src/Tasks/py",
          index: "functions/get_tasks.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: tasksTable.tableName,
          },
        });
        tasksTable.grantReadData(this.getTasksFn);

        this.deleteTaskFn = new pylambda.PythonFunction(this, "deleteTaskFn", {
          entry: "src/Tasks/py",
          index: "functions/delete_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: tasksTable.tableName,
          },
        });
        tasksTable.grantReadWriteData(this.deleteTaskFn);

        this.completeTaskFn = new pylambda.PythonFunction(this, "completeTaskFn", {
          entry: "src/Tasks/py",
          index: "functions/complete_task.py",
          runtime: lambda.Runtime.PYTHON_3_10,
          timeout: cdk.Duration.seconds(30),
          environment: {
            TABLE_NAME: tasksTable.tableName,
          },
        });
        tasksTable.grantReadWriteData(this.completeTaskFn);
    }
}