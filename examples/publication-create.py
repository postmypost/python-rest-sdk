#!/usr/bin/env python3

import sys
import os
import datetime
import postmypost_rest_sdk
from postmypost_rest_sdk.api.publications_api import PublicationsApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException
from postmypost_rest_sdk.models.create_publication_request import CreatePublicationRequest
from postmypost_rest_sdk.models.publication_detail_edit_request import PublicationDetailEditRequest
from postmypost_rest_sdk.models.publication_detail_publication_type_enum import PublicationDetailPublicationTypeEnum
from postmypost_rest_sdk.models.publication_status_enum_edit import PublicationStatusEnumEdit

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token and project ID
access_token = 'YOUR_API_ACCESS_TOKEN'
project_id = 123456

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Build the publication request object
publication_request = CreatePublicationRequest(
    project_id=project_id,
    post_at=datetime.datetime(2025, 6, 30, 12, 0, 0, tzinfo=datetime.timezone.utc),  # Publication time (UTC)
    account_ids=[111111, 222222],  # Example account IDs
    publication_status=PublicationStatusEnumEdit.PENDING_PUBLICATION,
    details=[
        PublicationDetailEditRequest(
            account_id=111111,
            publication_type=PublicationDetailPublicationTypeEnum.POST,
            content="Check out our new product launch! #newproduct #launch",
            file_ids=[42516053],
        ),
        PublicationDetailEditRequest(
            account_id=222222,
            publication_type=PublicationDetailPublicationTypeEnum.POST,
            link="https://example.com/new-product",
        ),
    ]
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the PublicationsApi with the api_client
    publications_api = PublicationsApi(api_client)

    try:
        response = publications_api.create_publication(publication_request)
        print("Publication created successfully!")
        print(f"  Publication ID: {response.id}")
    except ApiException as e:
        print(f"Error while creating publication: {e}")
