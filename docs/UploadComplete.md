# UploadComplete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_complete import UploadComplete

# TODO update the JSON string below
json = "{}"
# create an instance of UploadComplete from a JSON string
upload_complete_instance = UploadComplete.from_json(json)
# print the JSON string representation of the object
print(UploadComplete.to_json())

# convert the object into a dict
upload_complete_dict = upload_complete_instance.to_dict()
# create an instance of UploadComplete from a dict
upload_complete_from_dict = UploadComplete.from_dict(upload_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


