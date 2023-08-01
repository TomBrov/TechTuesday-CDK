import datetime
import os
from json import JSONEncoder

import boto3
import yaml
from aws_lambda_typing import context, events, responses

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Swagger UI</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui.css" >
  <style>
    html
    {
      box-sizing: border-box;
      overflow: -moz-scrollbars-vertical;
      overflow-y: scroll;
    }
    *,
    *:before,
    *:after
    {
      box-sizing: inherit;
    }

    body {
      margin:0;
      background: #fafafa;
    }
  </style>
</head>
<body>

<div id="swagger-ui"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui-bundle.js"> </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {

  var spec = %s;

  // Build a system
  const ui = SwaggerUIBundle({
    spec: spec,
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })

  window.ui = ui
}
</script>
</body>

</html>
"""


class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return JSONEncoder.default(self, o)


def convert_openapi_yaml_to_html(yaml_data):
    spec = yaml.load(yaml_data, Loader=yaml.FullLoader)
    html = TEMPLATE % DateTimeEncoder().encode(spec)
    return html


def handler(event: events.APIGatewayProxyEventV1, ctx: context.Context) -> responses.APIGatewayProxyResponseV1:
    s3 = boto3.resource("s3")
    bucket_name = os.getenv("BUCKET_NAME")
    object_key = os.getenv("KEY")

    obj = s3.Object(bucket_name, object_key)
    data = obj.get()["Body"].read().decode("utf-8")

    html = convert_openapi_yaml_to_html(data)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "multiValueHeaders": {},
        "body": html,
    }
