# postmypost_rest_sdk.UploadApi

All URIs are relative to *https://api.postmypost.io/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_upload**](UploadApi.md#complete_upload) | **POST** /upload/complete | Complete file upload
[**init_upload**](UploadApi.md#init_upload) | **POST** /upload/init | Initialize file upload
[**status_upload**](UploadApi.md#status_upload) | **GET** /upload/status | Check file upload status


# **complete_upload**
> UploadComplete complete_upload(id)

Complete file upload

Completes the file upload process after the file has been successfully sent.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.upload_complete import UploadComplete
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
    api_instance = postmypost_rest_sdk.UploadApi(api_client)
    id = 56 # int | Upload ID obtained during initialization

    try:
        # Complete file upload
        api_response = api_instance.complete_upload(id)
        print("The response of UploadApi->complete_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->complete_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Upload ID obtained during initialization | 

### Return type

[**UploadComplete**](UploadComplete.md)

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

# **init_upload**
> UploadInit init_upload(init_upload_request)

Initialize file upload

Initializes the file upload process.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest
from postmypost_rest_sdk.models.upload_init import UploadInit
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
    api_instance = postmypost_rest_sdk.UploadApi(api_client)
    init_upload_request = postmypost_rest_sdk.InitUploadRequest() # InitUploadRequest | Initializes the file upload process. Requires one of the following parameter combinations: - `project_id` and `url` - `project_id`, `name`, and `size` 

    try:
        # Initialize file upload
        api_response = api_instance.init_upload(init_upload_request)
        print("The response of UploadApi->init_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->init_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **init_upload_request** | [**InitUploadRequest**](InitUploadRequest.md)| Initializes the file upload process. Requires one of the following parameter combinations: - &#x60;project_id&#x60; and &#x60;url&#x60; - &#x60;project_id&#x60;, &#x60;name&#x60;, and &#x60;size&#x60;  | 

### Return type

[**UploadInit**](UploadInit.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **status_upload**
> UploadStatus status_upload(id)

Check file upload status

Checks the processing status of an uploaded file.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.upload_status import UploadStatus
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
    api_instance = postmypost_rest_sdk.UploadApi(api_client)
    id = 56 # int | Upload ID obtained during initialization

    try:
        # Check file upload status
        api_response = api_instance.status_upload(id)
        print("The response of UploadApi->status_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->status_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Upload ID obtained during initialization | 

### Return type

[**UploadStatus**](UploadStatus.md)

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

