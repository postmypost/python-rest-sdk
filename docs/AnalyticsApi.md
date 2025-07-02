# postmypost_rest_sdk.AnalyticsApi

All URIs are relative to *https://api.postmypost.io/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics_accounts**](AnalyticsApi.md#get_analytics_accounts) | **GET** /analytics/accounts | Get account analytics
[**get_analytics_publications**](AnalyticsApi.md#get_analytics_publications) | **GET** /analytics/publications | Get publications analytics


# **get_analytics_accounts**
> AccountAnalyticsResponse get_analytics_accounts(project_id, account_id, date_from, date_to, metrics)

Get account analytics

Retrieve account metrics (e.g., number of followers) for a specified period.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.account_analytics_response import AccountAnalyticsResponse
from postmypost_rest_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.postmypost.io/v4.1
# See configuration.py for a list of all supported configuration parameters.
configuration = postmypost_rest_sdk.Configuration(
    host = "https://api.postmypost.io/v4.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = postmypost_rest_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = postmypost_rest_sdk.AnalyticsApi(api_client)
    project_id = 56 # int | Project ID
    account_id = 'account_id_example' # str | Account ID
    date_from = '2013-10-20' # date | Start date of the period (YYYY-MM-DD)
    date_to = '2013-10-20' # date | End date of the period (YYYY-MM-DD)
    metrics = 'metrics_example' # str | Comma-separated list of metrics (e.g., followers,subscribed)

    try:
        # Get account analytics
        api_response = api_instance.get_analytics_accounts(project_id, account_id, date_from, date_to, metrics)
        print("The response of AnalyticsApi->get_analytics_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_analytics_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **account_id** | **str**| Account ID | 
 **date_from** | **date**| Start date of the period (YYYY-MM-DD) | 
 **date_to** | **date**| End date of the period (YYYY-MM-DD) | 
 **metrics** | **str**| Comma-separated list of metrics (e.g., followers,subscribed) | 

### Return type

[**AccountAnalyticsResponse**](AccountAnalyticsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analytics_publications**
> PublicationAnalyticsResponse get_analytics_publications(project_id, account_id, date_from, date_to)

Get publications analytics

Retrieve post analytics by account and project for a specified period.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.publication_analytics_response import PublicationAnalyticsResponse
from postmypost_rest_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.postmypost.io/v4.1
# See configuration.py for a list of all supported configuration parameters.
configuration = postmypost_rest_sdk.Configuration(
    host = "https://api.postmypost.io/v4.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = postmypost_rest_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with postmypost_rest_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = postmypost_rest_sdk.AnalyticsApi(api_client)
    project_id = 56 # int | Project ID
    account_id = 'account_id_example' # str | Account ID
    date_from = '2013-10-20' # date | Start date of the period (YYYY-MM-DD)
    date_to = '2013-10-20' # date | End date of the period (YYYY-MM-DD)

    try:
        # Get publications analytics
        api_response = api_instance.get_analytics_publications(project_id, account_id, date_from, date_to)
        print("The response of AnalyticsApi->get_analytics_publications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_analytics_publications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **account_id** | **str**| Account ID | 
 **date_from** | **date**| Start date of the period (YYYY-MM-DD) | 
 **date_to** | **date**| End date of the period (YYYY-MM-DD) | 

### Return type

[**PublicationAnalyticsResponse**](PublicationAnalyticsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

