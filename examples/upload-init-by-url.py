#!/usr/bin/env python3

import sys
import os

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest

# Set your API access token and project ID
access_token = 'YOUR_ACCESS_TOKEN'
project_id = 123456

# Example image URL (replace with your file if needed)
file_url = 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Example.jpg'

# Configure the SDK
config = Configuration()
config.access_token = access_token

# Create an instance of the UploadApi
upload_api = UploadApi(config)

try:
    upload_request = InitUploadRequest(
        project_id=project_id,
        url=file_url,
    )

    response = upload_api.init_upload(upload_request)

    print("Upload initialized successfully.")
    print(f"  Upload ID: {response.id}")
    print(f"  Upload status: {response.status}")
except ApiException as e:
    print(f"Error during file upload: {e}")