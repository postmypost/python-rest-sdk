# UploadInitOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**name** | **str** | File name | 
**size** | **int** | File size in bytes | 
**action** | **str** | Upload URL | 
**fields** | [**List[UploadInitOneOf1FieldsInner]**](UploadInitOneOf1FieldsInner.md) | Parameters to be sent with the file upload | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_init_one_of1 import UploadInitOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInitOneOf1 from a JSON string
upload_init_one_of1_instance = UploadInitOneOf1.from_json(json)
# print the JSON string representation of the object
print(UploadInitOneOf1.to_json())

# convert the object into a dict
upload_init_one_of1_dict = upload_init_one_of1_instance.to_dict()
# create an instance of UploadInitOneOf1 from a dict
upload_init_one_of1_from_dict = UploadInitOneOf1.from_dict(upload_init_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


