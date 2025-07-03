#!/usr/bin/env python3

import sys
import os
import postmypost_rest_sdk
from postmypost_rest_sdk.api.publications_api import PublicationsApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token and project ID
access_token = 'YOUR_API_ACCESS_TOKEN'
project_id = 123456

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the PublicationsApi with the api_client
    publications_api = PublicationsApi(api_client)

    try:
        # Get publications for the specified project
        publications_response = publications_api.get_publications(project_id)

        print("Publications list:")

        for publication in publications_response.data:
            print(f"  - ID: {publication.id} | Date: {publication.post_at.strftime('%Y-%m-%d %H:%M')}")

        # Output pagination info
        pagination = publications_response.pages
        print("\nPagination:")
        print(f"  Page: {pagination.page} | Per page: {pagination.per_page} | "
              f"Total pages: {pagination.total_pages} | Total count: {pagination.total_count}")

        if pagination.prev is not None:
            print(f"  Prev: {pagination.prev}")

        if pagination.next is not None:
            print(f"  Next: {pagination.next}")

    except ApiException as e:
        print(f"Error while requesting publications: {e}")