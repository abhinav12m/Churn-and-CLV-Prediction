import boto3
import sagemaker
from sagemaker.model import Model

s3_bucket = "bank-churn-models"
role = "arn:aws:iam::203918865660:role/SageMakerExecutionRole"

clv_model = Model(
    model_data=f"s3://{s3_bucket}/models/clv_model.tar.gz",
    role=role,
    image_uri="683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn"
)
clv_model.deploy(initial_instance_count=1, instance_type="ml.m5.large", endpoint_name="clv-endpoint")

churn_model = Model(
    model_data=f"s3://{s3_bucket}/models/churn_model.tar.gz",
    role=role,
    image_uri="683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn"
)
churn_model.deploy(initial_instance_count=1, instance_type="ml.m5.large", endpoint_name="churn-endpoint")

print("Models deployed on SageMaker!")
