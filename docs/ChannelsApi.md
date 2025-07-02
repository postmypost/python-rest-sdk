# postmypost_rest_sdk.ChannelsApi

All URIs are relative to *https://api.postmypost.io/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channels**](ChannelsApi.md#get_channels) | **GET** /channels | Get list of channels


# **get_channels**
> ChannelsResponse get_channels(sort=sort, page=page, per_page=per_page)

Get list of channels

Retrieve a list of all available channels in the system.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.channels_response import ChannelsResponse
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
    api_instance = postmypost_rest_sdk.ChannelsApi(api_client)
    sort = 'sort_example' # str | List sorting parameter. Format: `sort=field` — ascending by field, `sort=-field` — descending by field. Multiple fields can be specified separated by a comma: `sort=field,-another_field`.  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    per_page = 20 # int | Number of items per page (maximum 50). (optional) (default to 20)

    try:
        # Get list of channels
        api_response = api_instance.get_channels(sort=sort, page=page, per_page=per_page)
        print("The response of ChannelsApi->get_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| List sorting parameter. Format: &#x60;sort&#x3D;field&#x60; — ascending by field, &#x60;sort&#x3D;-field&#x60; — descending by field. Multiple fields can be specified separated by a comma: &#x60;sort&#x3D;field,-another_field&#x60;.  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **per_page** | **int**| Number of items per page (maximum 50). | [optional] [default to 20]

### Return type

[**ChannelsResponse**](ChannelsResponse.md)

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

