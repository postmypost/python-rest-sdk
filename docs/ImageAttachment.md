# ImageAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**image** | [**MediaFile**](MediaFile.md) |  | 
**preview** | [**MediaFile**](MediaFile.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.image_attachment import ImageAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttachment from a JSON string
image_attachment_instance = ImageAttachment.from_json(json)
# print the JSON string representation of the object
print(ImageAttachment.to_json())

# convert the object into a dict
image_attachment_dict = image_attachment_instance.to_dict()
# create an instance of ImageAttachment from a dict
image_attachment_from_dict = ImageAttachment.from_dict(image_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


