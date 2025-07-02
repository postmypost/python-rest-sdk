# InitUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID Project | 
**url** | **str** | File URL | 
**name** | **str** | File name | 
**size** | **int** | File size in bytes | 

## Example

```python
from postmypost_rest_sdk.models.init_upload_request import InitUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitUploadRequest from a JSON string
init_upload_request_instance = InitUploadRequest.from_json(json)
# print the JSON string representation of the object
print(InitUploadRequest.to_json())

# convert the object into a dict
init_upload_request_dict = init_upload_request_instance.to_dict()
# create an instance of InitUploadRequest from a dict
init_upload_request_from_dict = InitUploadRequest.from_dict(init_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


