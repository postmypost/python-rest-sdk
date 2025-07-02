# UploadInitOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**name** | **str** | File name | 
**url** | **str** | URL to the uploaded file | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_init_one_of import UploadInitOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInitOneOf from a JSON string
upload_init_one_of_instance = UploadInitOneOf.from_json(json)
# print the JSON string representation of the object
print(UploadInitOneOf.to_json())

# convert the object into a dict
upload_init_one_of_dict = upload_init_one_of_instance.to_dict()
# create an instance of UploadInitOneOf from a dict
upload_init_one_of_from_dict = UploadInitOneOf.from_dict(upload_init_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


