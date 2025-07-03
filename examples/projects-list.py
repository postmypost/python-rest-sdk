#!/usr/bin/env python3

import sys
import os
import postmypost_rest_sdk
from postmypost_rest_sdk.api.projects_api import ProjectsApi
from postmypost_rest_sdk.configuration import Configuration
from postmypost_rest_sdk.exceptions import ApiException

# Add the parent directory to the Python path to import the SDK
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set your API access token
access_token = 'YOUR_API_ACCESS_TOKEN'

# Configure the SDK
configuration = Configuration(
    access_token=access_token
)

# Create API client context
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the ProjectsApi with the api_client
    projects_api = ProjectsApi(api_client)

    try:
        # Get projects
        projects_response = projects_api.get_projects()

        print("Projects list:")

        for project in projects_response.data:
            print(f"  - ID: {project.id} | Name: {project.name}")

        # Output pagination info
        pagination = projects_response.pages
        print("\nPagination:")
        print(f"  Page: {pagination.page} | Per page: {pagination.per_page} | "
              f"Total pages: {pagination.total_pages} | Total count: {pagination.total_count}")

        if pagination.prev is not None:
            print(f"  Prev: {pagination.prev}")

        if pagination.next is not None:
            print(f"  Next: {pagination.next}")

    except ApiException as e:
        print(f"Error while requesting projects: {e}")
