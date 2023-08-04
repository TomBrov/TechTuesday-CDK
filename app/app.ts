import * as cdk from "aws-cdk-lib";
import "source-map-support/register";
import { TasksStack } from "./stacks/tasks-service";
import { ApiStack } from "./stacks/api-stack";

const app = new cdk.App();
const tasks = new TasksStack(app, "TasksStack");
const api = new ApiStack(app, "ApiStack", {
    createTaskFn: tasks.createTaskFn,
    getTaskFn: tasks.getTaskFn,
    getTasksFn: tasks.getTasksFn,
    updateTaskFn: tasks.updateTaskFn,
    deleteTaskFn: tasks.deleteTaskFn,
    completeTaskFn: tasks.completeTaskFn,
});