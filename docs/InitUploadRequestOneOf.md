# InitUploadRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID Project | 
**url** | **str** | File URL | 

## Example

```python
from postmypost_rest_sdk.models.init_upload_request_one_of import InitUploadRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of InitUploadRequestOneOf from a JSON string
init_upload_request_one_of_instance = InitUploadRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(InitUploadRequestOneOf.to_json())

# convert the object into a dict
init_upload_request_one_of_dict = init_upload_request_one_of_instance.to_dict()
# create an instance of InitUploadRequestOneOf from a dict
init_upload_request_one_of_from_dict = InitUploadRequestOneOf.from_dict(init_upload_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


