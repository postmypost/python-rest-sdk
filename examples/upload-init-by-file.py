#!/usr/bin/env python3

import sys
import os
import requests

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest

# Set your API access token and project ID
access_token = 'YOUR_ACCESS_TOKEN'
project_id = 123456

# Path to your local file
file_path = '/path/to/your/file.jpg'

# Check if file exists
if not os.path.exists(file_path):
    raise Exception(f"File does not exist: {file_path}")

file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)

# Configure the SDK
config = Configuration()
config.access_token = access_token

# Create an instance of the UploadApi
upload_api = UploadApi(config)

try:
    # Step 1: Initialize upload
    upload_request = InitUploadRequest(
        project_id=project_id,
        name=file_name,
        size=file_size,
    )

    init_response = upload_api.init_upload(upload_request)
    print("Upload initialized successfully.")
    print(f"  Upload ID: {init_response.id}")
    print(f"  Upload status: {init_response.status}")

    # Step 2: Prepare multipart form data for S3
    form_data = {}
    files = {}
    
    # Add all fields from the response
    for field in init_response.fields:
        form_data[field.key] = field.value
    
    # Add the file
    with open(file_path, 'rb') as file:
        files = {'file': (file_name, file, 'application/octet-stream')}
    
    # Step 3: Upload file to S3
    s3_response = requests.post(
        init_response.action,
        data=form_data,
        files=files
    )
    
    # Check if the upload was successful
    if s3_response.status_code not in (200, 201, 204):
        raise Exception(f"S3 upload failed with status code: {s3_response.status_code}")
    
    print("File uploaded to storage provider (S3).")
    
    # Step 4: Complete the upload via Postmypost API
    complete_response = upload_api.complete_upload(init_response.id)
    print("Upload completed successfully!")
    print(f"  Upload ID:    {complete_response.id}")
    print(f"  Status code:  {complete_response.status}")

except ApiException as e:
    print(f"Error during file upload: {e}")
except Exception as e:
    print(f"Error during file upload: {e}")