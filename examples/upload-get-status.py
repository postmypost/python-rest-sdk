#!/usr/bin/env python3

import sys
import os
import postmypost_rest_sdk
from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token and the upload ID you want to check
access_token = 'YOUR_API_ACCESS_TOKEN'
upload_id = 123456

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the UploadApi with the api_client
    upload_api = UploadApi(api_client)

    try:
        response = upload_api.status_upload(upload_id)

        print("Upload status received successfully.")
        print(f"  Upload ID:    {response.id}")
        print(f"  File ID:      {response.file_id}")
        print(f"  Status code:  {response.status}")
        # You can map status codes to human-readable messages here if needed.
    except ApiException as e:
        print(f"Error while requesting upload status: {e}")
