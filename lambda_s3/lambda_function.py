import json
import boto3
from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = "rohit-expense-tracker-s3"

def lambda_handler(event, context):
    expense = event.get("expense", {})

    expense_id = expense.get("id", "unknown")
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    file_name = f"expense-backups/expense-{expense_id}-{timestamp}.json"

    backup_data = {
        "message": "Expense backed up successfully",
        "expense": expense,
        "backup_timestamp": datetime.utcnow().isoformat()
    }

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(backup_data),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Expense backup uploaded to S3",
            "s3_key": file_name
        })
    }