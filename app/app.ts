import * as cdk from "aws-cdk-lib";
import "source-map-support/register";
import { RunnersStack } from "../lib/runners-stack";

const app = new cdk.App();
new RunnersStack(app, "RunnersStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});