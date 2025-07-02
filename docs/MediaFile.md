# MediaFile

Media file (image or video) used as an attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | File width in pixels | [optional] 
**height** | **int** | File height in pixels | [optional] 
**url** | **str** | URL to download or view the file | [optional] 

## Example

```python
from postmypost_rest_sdk.models.media_file import MediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFile from a JSON string
media_file_instance = MediaFile.from_json(json)
# print the JSON string representation of the object
print(MediaFile.to_json())

# convert the object into a dict
media_file_dict = media_file_instance.to_dict()
# create an instance of MediaFile from a dict
media_file_from_dict = MediaFile.from_dict(media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


