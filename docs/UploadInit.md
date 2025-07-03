# UploadInit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**url** | **str** | URL of the uploaded file | 
**size** | **int** | File size in bytes | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 
**name** | **str** | File name | 
**action** | **str** | Upload endpoint URL | 
**fields** | [**List[UploadByFileFieldsInner]**](UploadByFileFieldsInner.md) | Parameters to be submitted with the file during upload | 

## Example

```python
from postmypost_rest_sdk.models.upload_init import UploadInit

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInit from a JSON string
upload_init_instance = UploadInit.from_json(json)
# print the JSON string representation of the object
print(UploadInit.to_json())

# convert the object into a dict
upload_init_dict = upload_init_instance.to_dict()
# create an instance of UploadInit from a dict
upload_init_from_dict = UploadInit.from_dict(upload_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


