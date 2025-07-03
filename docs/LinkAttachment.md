# LinkAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**link** | [**Link**](Link.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.link_attachment import LinkAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAttachment from a JSON string
link_attachment_instance = LinkAttachment.from_json(json)
# print the JSON string representation of the object
print(LinkAttachment.to_json())

# convert the object into a dict
link_attachment_dict = link_attachment_instance.to_dict()
# create an instance of LinkAttachment from a dict
link_attachment_from_dict = LinkAttachment.from_dict(link_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


