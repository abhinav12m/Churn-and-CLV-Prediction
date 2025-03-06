import json
import boto3

sagemaker_runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    model_name = event["model"]
    payload = json.dumps(event["data"])
    endpoint_name = "clv-endpoint" if model_name == "clv" else "churn-endpoint"

    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=payload
    )

    result = json.loads(response["Body"].read().decode())

    return {"statusCode": 200, "prediction": result}
