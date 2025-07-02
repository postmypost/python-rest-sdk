# InitUploadRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID Project | 
**name** | **str** | File name | 
**size** | **int** | File size in bytes | 

## Example

```python
from postmypost_rest_sdk.models.init_upload_request_one_of1 import InitUploadRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InitUploadRequestOneOf1 from a JSON string
init_upload_request_one_of1_instance = InitUploadRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(InitUploadRequestOneOf1.to_json())

# convert the object into a dict
init_upload_request_one_of1_dict = init_upload_request_one_of1_instance.to_dict()
# create an instance of InitUploadRequestOneOf1 from a dict
init_upload_request_one_of1_from_dict = InitUploadRequestOneOf1.from_dict(init_upload_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


