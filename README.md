# List Cloud Resources ☁️

A Python script that connects to AWS and lists S3 buckets and EC2 instances using boto3.

## What it does
- Connects to AWS using the official Python SDK (boto3)
- Lists all S3 storage buckets in the account
- Lists all EC2 (virtual server) instances and their status

## How to run
1. Install dependencies: `pip install boto3`
2. Configure AWS credentials: `aws configure`
3. Run the script: `python3 list_resources.py`

## What I learned
- Setting up an AWS IAM user with least-privilege (read-only) access
- Configuring AWS CLI credentials securely
- Using boto3 to interact with AWS services programmatically
- Basic cloud resource auditing
