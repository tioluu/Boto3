# This script lists all S3 buckets in the AWS account using Boto3.
import boto3  # AWS SDK for Python

# Create an S3 resource object
s3_resource = boto3.resource('s3')

# Create an S3 client object
s3_client = boto3.client('s3')

bucket_name = 'testfordevopsbucket'

# response = s3_client.create_bucket(
#     Bucket=bucket_name,)

# print(f"Bucket '{bucket_name}' created.")

path = 'cv.docx'
s3_key = 'cv/mycv.docx'

# List all buckets using the client
response = s3_client.list_buckets()

# Get the display name of the bucket owner
owner = response['Owner']['DisplayName']

# Iterate through all buckets using the resource object
for bucket in s3_resource.buckets.all():
    # Print bucket name, creation date, and owner
    print(f"Name: {bucket.name}, Date:{bucket.creation_date}, Owner: {owner}")
    print(f"Items: {bucket.objects.all()}")

print(f"Items in bucket: {bucket_name}")
for obj in bucket.objects.all():
    print(f"- {obj.key} ({obj.size} bytes)")




# # Upload a file to all buckets
# for bucket in s3_resource.buckets.all():
#     try:
#         s3_client.upload_file (path, bucket.name, s3_key)
#         print(f"File {path} has been uploaded to bucket {bucket.name} with key {s3_key}.")
#     except Exception as e:
#         print(f"Failed to upload {path} to bucket {bucket.name}: {e}")

# bucket_name = 'my-uniqueghahahh'
# # delete all objects
# bucket.objects.all().delete()

# # delete the bucket itself
# bucket.delete()

# print(f"✅ Bucket '{bucket.name}' and all its contents deleted.")


# bucket_name = 'my-uniquehahahh'
# # delete all objects
# bucket.objects.all().delete()

# # delete the bucket itself
# bucket.delete()

# print(f"✅ Bucket '{bucket.name}' and all its contents deleted.")


