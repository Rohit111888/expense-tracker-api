import json
import boto3

lambda_client = boto3.client(
    "lambda",
    region_name="us-east-1"
)


def export_expenses_to_s3(expenses):

    response = lambda_client.invoke(
        FunctionName="expense-s3-reader",
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "expenses": expenses
        })
    )

    payload = json.loads(
        response["Payload"].read()
    )

    return payload