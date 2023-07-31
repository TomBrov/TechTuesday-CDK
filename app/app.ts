import * as cdk from "aws-cdk-lib";
import "source-map-support/register";
import { RunnersStack } from "../lib/runners-stack";

const app = new cdk.App();
const tasks = new TasksStack(app, "TasksStack", {});
const api = new ApiStack(app, "ApiStack", {
    createTaskFn: tasks.createTaskFn
    getTaskFn: tasks.getTaskFn
    getTasksFn: tasks.getTasksFn
    updateTaskFn: tasks.updateTaskFn
    deleteTaskFn: tasks.deleteTaskFn
    completeTaskFn: tasks.completeTaskFn
});