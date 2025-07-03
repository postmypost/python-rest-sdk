# InitUploadByUrlRequest

Request to initialize file upload by URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID Project | 
**url** | **str** | File URL | 

## Example

```python
from postmypost_rest_sdk.models.init_upload_by_url_request import InitUploadByUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitUploadByUrlRequest from a JSON string
init_upload_by_url_request_instance = InitUploadByUrlRequest.from_json(json)
# print the JSON string representation of the object
print(InitUploadByUrlRequest.to_json())

# convert the object into a dict
init_upload_by_url_request_dict = init_upload_by_url_request_instance.to_dict()
# create an instance of InitUploadByUrlRequest from a dict
init_upload_by_url_request_from_dict = InitUploadByUrlRequest.from_dict(init_upload_by_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


