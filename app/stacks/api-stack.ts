import * as golambda from "@aws-cdk/aws-lambda-go-alpha";
import * as pylambda from "@aws-cdk/aws-lambda-python-alpha";
import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Asset } from "aws-cdk-lib/aws-s3-assets";
import { Construct } from "constructs";

export class ApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: ApiStackProps) {
    super(scope, id, props);

    // Stack tags
    cdk.Tags.of(this).add("App", "ApiStack");

    // OpenAPI docs
    const openApiSpec = new Asset(this, "OpenApiAsset", {
      path: "docs/openapi.yaml",
    });

    // Docs lambda function
    const docsFn = new pylambda.PythonFunction(this, "DocsFn", {
      entry: "src/py",
      index: "api/serve_docs.py",
      runtime: lambda.Runtime.PYTHON_3_10,
      timeout: cdk.Duration.seconds(5),
      environment: {
        BUCKET_NAME: openApiSpec.s3BucketName,
        KEY: openApiSpec.s3ObjectKey,
      },
      tracing: Tracing.ACTIVE,
      currentVersionOptions: {
        provisionedConcurrentExecutions: 1,
      },
    });
    openApiSpec.grantRead(docsFn);

    const healthFn = new pylambda.PythonFunction(this, "HealthFn", {
      entry: "src/py",
      index: "api/health.py",
      runtime: lambda.Runtime.PYTHON_3_10,
      timeout: cdk.Duration.seconds(30),
    });

    // API Gateway
    const api = new apigateway.RestApi(this, "ApiGateway", {
      defaultCorsPreflightOptions: {
        allowOrigins: apigateway.Cors.ALL_ORIGINS,
        allowMethods: apigateway.Cors.ALL_METHODS,
      },
      endpointConfiguration: {
        types: [apigateway.EndpointType.EDGE],
      },
    });
    const v1 = api.root.addResource("api").addResource("v1");
    const tasks =
    const docs = api.root.addResource("docs");
  }
}