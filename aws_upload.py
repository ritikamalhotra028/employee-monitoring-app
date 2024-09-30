# modules/aws_upload.py
import boto3
import os

def upload_to_s3(file_name, bucket_name, s3_file_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, s3_file_name)
        print(f"Upload Successful: {s3_file_name}")
    except Exception as e:
        print(f"Upload Failed: {e}")
