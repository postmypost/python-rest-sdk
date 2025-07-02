# UploadStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**file_id** | **int** | File ID | [optional] 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_status import UploadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStatus from a JSON string
upload_status_instance = UploadStatus.from_json(json)
# print the JSON string representation of the object
print(UploadStatus.to_json())

# convert the object into a dict
upload_status_dict = upload_status_instance.to_dict()
# create an instance of UploadStatus from a dict
upload_status_from_dict = UploadStatus.from_dict(upload_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


