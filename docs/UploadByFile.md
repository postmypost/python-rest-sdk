# UploadByFile

Parameters required for direct file upload to storage (e.g., S3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**name** | **str** | File name | 
**size** | **int** | File size in bytes | 
**action** | **str** | Upload endpoint URL | 
**fields** | [**List[UploadByFileFieldsInner]**](UploadByFileFieldsInner.md) | Parameters to be submitted with the file during upload | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_by_file import UploadByFile

# TODO update the JSON string below
json = "{}"
# create an instance of UploadByFile from a JSON string
upload_by_file_instance = UploadByFile.from_json(json)
# print the JSON string representation of the object
print(UploadByFile.to_json())

# convert the object into a dict
upload_by_file_dict = upload_by_file_instance.to_dict()
# create an instance of UploadByFile from a dict
upload_by_file_from_dict = UploadByFile.from_dict(upload_by_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


