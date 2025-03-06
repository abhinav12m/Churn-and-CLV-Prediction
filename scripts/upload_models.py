import boto3

s3 = boto3.client("s3")
bucket_name = "bank-churn-models"

s3.upload_file("models/clv_model.tar.gz", bucket_name, "models/clv_model.tar.gz")
s3.upload_file("models/churn_model.tar.gz", bucket_name, "models/churn_model.tar.gz")

print("Models uploaded to S3!")