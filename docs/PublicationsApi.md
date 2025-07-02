# postmypost_rest_sdk.PublicationsApi

All URIs are relative to *https://api.postmypost.io/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_publication**](PublicationsApi.md#create_publication) | **POST** /publications | Create publication
[**delete_publication**](PublicationsApi.md#delete_publication) | **DELETE** /publications/{id} | Delete publication
[**get_publication**](PublicationsApi.md#get_publication) | **GET** /publications/{id} | Get publication by ID
[**get_publications**](PublicationsApi.md#get_publications) | **GET** /publications | Get list of publications
[**update_publication**](PublicationsApi.md#update_publication) | **PUT** /publications/{id} | Update publication


# **create_publication**
> Publication create_publication(create_publication_request)

Create publication

Create a new publication.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.create_publication_request import CreatePublicationRequest
from postmypost_rest_sdk.models.publication import Publication
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
    api_instance = postmypost_rest_sdk.PublicationsApi(api_client)
    create_publication_request = postmypost_rest_sdk.CreatePublicationRequest() # CreatePublicationRequest | 

    try:
        # Create publication
        api_response = api_instance.create_publication(create_publication_request)
        print("The response of PublicationsApi->create_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->create_publication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_publication_request** | [**CreatePublicationRequest**](CreatePublicationRequest.md)|  | 

### Return type

[**Publication**](Publication.md)

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

# **delete_publication**
> Publication delete_publication(id, delete_option, account_ids)

Delete publication

Delete a publication.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.publication import Publication
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
    api_instance = postmypost_rest_sdk.PublicationsApi(api_client)
    id = 56 # int | Publication ID
    delete_option = 56 # int | Deletion method: 1 — delete everywhere, 2 — only in social network, 3 — only in Postmypost 
    account_ids = 'account_ids_example' # str | Comma-separated list of account IDs

    try:
        # Delete publication
        api_response = api_instance.delete_publication(id, delete_option, account_ids)
        print("The response of PublicationsApi->delete_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->delete_publication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Publication ID | 
 **delete_option** | **int**| Deletion method: 1 — delete everywhere, 2 — only in social network, 3 — only in Postmypost  | 
 **account_ids** | **str**| Comma-separated list of account IDs | 

### Return type

[**Publication**](Publication.md)

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

# **get_publication**
> Publication get_publication(id)

Get publication by ID

Retrieve publication data by its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.publication import Publication
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
    api_instance = postmypost_rest_sdk.PublicationsApi(api_client)
    id = 56 # int | Publication ID

    try:
        # Get publication by ID
        api_response = api_instance.get_publication(id)
        print("The response of PublicationsApi->get_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->get_publication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Publication ID | 

### Return type

[**Publication**](Publication.md)

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

# **get_publications**
> PublicationsResponse get_publications(project_id, post_date=post_date, sort=sort, page=page, per_page=per_page)

Get list of publications

Retrieve a list of all publications available in the system.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.publications_response import PublicationsResponse
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
    api_instance = postmypost_rest_sdk.PublicationsApi(api_client)
    project_id = 56 # int | Project ID
    post_date = '2013-10-20' # date | Publication date (YYYY-MM-DD) (optional)
    sort = 'sort_example' # str | List sorting parameter. Format: `sort=field` — ascending by field, `sort=-field` — descending by field. Multiple fields can be specified separated by a comma: `sort=field,-another_field`.  (optional)
    page = 1 # int | Page number (starts from 1). (optional) (default to 1)
    per_page = 20 # int | Number of items per page (maximum 50). (optional) (default to 20)

    try:
        # Get list of publications
        api_response = api_instance.get_publications(project_id, post_date=post_date, sort=sort, page=page, per_page=per_page)
        print("The response of PublicationsApi->get_publications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->get_publications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **post_date** | **date**| Publication date (YYYY-MM-DD) | [optional] 
 **sort** | **str**| List sorting parameter. Format: &#x60;sort&#x3D;field&#x60; — ascending by field, &#x60;sort&#x3D;-field&#x60; — descending by field. Multiple fields can be specified separated by a comma: &#x60;sort&#x3D;field,-another_field&#x60;.  | [optional] 
 **page** | **int**| Page number (starts from 1). | [optional] [default to 1]
 **per_page** | **int**| Number of items per page (maximum 50). | [optional] [default to 20]

### Return type

[**PublicationsResponse**](PublicationsResponse.md)

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

# **update_publication**
> Publication update_publication(id, update_publication_request)

Update publication

Update a publication by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import postmypost_rest_sdk
from postmypost_rest_sdk.models.publication import Publication
from postmypost_rest_sdk.models.update_publication_request import UpdatePublicationRequest
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
    api_instance = postmypost_rest_sdk.PublicationsApi(api_client)
    id = 56 # int | Publication ID
    update_publication_request = postmypost_rest_sdk.UpdatePublicationRequest() # UpdatePublicationRequest | 

    try:
        # Update publication
        api_response = api_instance.update_publication(id, update_publication_request)
        print("The response of PublicationsApi->update_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->update_publication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Publication ID | 
 **update_publication_request** | [**UpdatePublicationRequest**](UpdatePublicationRequest.md)|  | 

### Return type

[**Publication**](Publication.md)

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

