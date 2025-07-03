# Attachment

Attachment to a post

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**image** | [**MediaFile**](MediaFile.md) |  | 
**preview** | [**MediaFile**](MediaFile.md) |  | 
**video** | [**MediaFile**](MediaFile.md) |  | 
**link** | [**Link**](Link.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


