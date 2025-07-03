# UploadByUrl

Details of a successfully uploaded file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Upload ID | 
**url** | **str** | URL of the uploaded file | 
**size** | **int** | File size in bytes | 
**status** | [**UploadStatusEnum**](UploadStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.upload_by_url import UploadByUrl

# TODO update the JSON string below
json = "{}"
# create an instance of UploadByUrl from a JSON string
upload_by_url_instance = UploadByUrl.from_json(json)
# print the JSON string representation of the object
print(UploadByUrl.to_json())

# convert the object into a dict
upload_by_url_dict = upload_by_url_instance.to_dict()
# create an instance of UploadByUrl from a dict
upload_by_url_from_dict = UploadByUrl.from_dict(upload_by_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


