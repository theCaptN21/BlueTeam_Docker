#Script to upload files to S3 bucket
#!/usr/bin/env python3

import boto3

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Dockerfile",
    Bucket="docker0123",
    Key="Dockerfile")
    
  


