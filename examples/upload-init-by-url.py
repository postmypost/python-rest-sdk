#!/usr/bin/env python3

import sys
import os

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import postmypost_rest_sdk
from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest
from postmypost_rest_sdk.models.init_upload_by_url_request import InitUploadByUrlRequest

# Set your API access token and project ID
access_token = 'YOUR_API_ACCESS_TOKEN'
project_id = 123456

# Example image URL (replace with your file if needed)
file_url = 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Example.jpg'

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the UploadApi with the api_client
    upload_api = UploadApi(api_client)

    try:
        # Create an InitUploadByUrlRequest first
        upload_by_url_request = InitUploadByUrlRequest(
            project_id=project_id,
            url=file_url,
        )

        # Pass the InitUploadByUrlRequest to InitUploadRequest
        upload_request = InitUploadRequest(upload_by_url_request)

        response = upload_api.init_upload(upload_request)

        upload_info = response.actual_instance

        print("Upload initialized successfully.")
        print(f"  Upload ID: {upload_info.id}")
        print(f"  Upload status: {upload_info.status}")
    except ApiException as e:
        print(f"Error during file upload: {e}")
