#!/usr/bin/env python3

import sys
import os
import requests
import postmypost_rest_sdk
from postmypost_rest_sdk.api.upload_api import UploadApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest
from postmypost_rest_sdk.models.init_upload_by_file_request import InitUploadByFileRequest

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token and project ID
access_token = 'YOUR_API_ACCESS_TOKEN'
project_id = 123456

# Path to your local file
file_path = '/path/to/your/file.jpg'

# Check if file exists
if not os.path.exists(file_path):
    raise Exception(f"File does not exist: {file_path}")

file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the UploadApi with the api_client
    upload_api = UploadApi(api_client)

    try:
        # Step 1: Initialize upload
        file_request = InitUploadByFileRequest(
            project_id=project_id,
            name=file_name,
            size=file_size,
        )
        upload_request = InitUploadRequest(file_request)

        init_response = upload_api.init_upload(upload_request)

        upload_info = init_response.actual_instance

        print("Upload initialized successfully.")
        print(f"  Upload ID: {upload_info.id}")
        print(f"  Upload status: {upload_info.status}")

        # Step 2: Prepare multipart form data for S3
        form_data = {}
        files = {}

        # Add all fields from the response
        if upload_info.fields:
            for field in upload_info.fields:
                form_data[field.key] = field.value

        # Add the file
        with open(file_path, 'rb') as file:
            files = {'file': (file_name, file, 'application/octet-stream')}

            # Step 3: Upload file to S3
            s3_response = requests.post(
                upload_info.action,
                data=form_data,
                files=files
            )

            # Check if the upload was successful
            if s3_response.status_code not in (200, 201, 204):
                raise Exception(f"S3 upload failed with status code: {s3_response.status_code}")

        print("File uploaded to storage provider (S3).")

        # Step 4: Complete the upload via Postmypost API
        complete_response = upload_api.complete_upload(upload_info.id)
        print("Upload completed successfully!")
        print(f"  Upload ID:    {complete_response.id}")
        print(f"  Status code:  {complete_response.status}")

    except ApiException as e:
        import traceback
        print(f"Error during file upload: {e}")
        traceback.print_exc()
    except Exception as e:
        import traceback
        print(f"Error during file upload: {e}")
        traceback.print_exc()
