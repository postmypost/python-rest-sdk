#!/usr/bin/env python3

import sys
import os
import time
import postmypost_rest_sdk
from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.upload_status_enum import UploadStatusEnum

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token and the upload ID you want to check
access_token = 'YOUR_API_ACCESS_TOKEN'
upload_id = 123456
max_attempts = 10

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the UploadApi with the api_client
    upload_api = UploadApi(api_client)

    for attempt in range(1, max_attempts + 1):
        try:
            response = upload_api.status_upload(upload_id)
            status = response.status

            print(f"Attempt {attempt}")
            print(f"Upload status: {status}")

            if status == UploadStatusEnum.FILE_UPLOADED_SUCCESSFULLY:
                print(f"File ID: {response.file_id}")
                print("Upload completed successfully!")
                break

            if status == UploadStatusEnum.ERROR:
                print("Upload failed with error.")
                break

        except ApiException as e:
            print(f"Error while requesting upload status: {e}")
            break

        time.sleep(2)

    if attempt >= max_attempts:
        print(f"Upload did not complete after {max_attempts} attempts.")
