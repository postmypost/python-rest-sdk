# Attach

Attachment to a post

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Attachment type: image — image; video — video.  | 

## Example

```python
from postmypost_rest_sdk.models.attach import Attach

# TODO update the JSON string below
json = "{}"
# create an instance of Attach from a JSON string
attach_instance = Attach.from_json(json)
# print the JSON string representation of the object
print(Attach.to_json())

# convert the object into a dict
attach_dict = attach_instance.to_dict()
# create an instance of Attach from a dict
attach_from_dict = Attach.from_dict(attach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


