#!/usr/bin/env python3

import sys
import os
import postmypost_rest_sdk
from postmypost_rest_sdk.api.accounts_api import AccountsApi
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
    # Create an instance of the AccountsApi with the api_client
    accounts_api = AccountsApi(api_client)

    try:
        # Get accounts for the specified project
        accounts_response = accounts_api.get_accounts(project_id)

        print("Accounts list:")

        for account in accounts_response.data:
            print(f"  - ID: {account.id} | Name: {account.name}")

        # Output pagination info
        pagination = accounts_response.pages
        print("\nPagination:")
        print(f"  Page: {pagination.page} | Per page: {pagination.per_page} | "
              f"Total pages: {pagination.total_pages} | Total count: {pagination.total_count}")

        if pagination.prev is not None:
            print(f"  Prev: {pagination.prev}")

        if pagination.next is not None:
            print(f"  Next: {pagination.next}")

    except ApiException as e:
        print(f"Error while requesting accounts: {e}")