import boto3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

# This script lists all S3 buckets in the AWS account using Boto3.
# Make sure to have AWS credentials configured in your environment.

