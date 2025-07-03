# VideoAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**video** | [**MediaFile**](MediaFile.md) |  | 
**preview** | [**MediaFile**](MediaFile.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.video_attachment import VideoAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAttachment from a JSON string
video_attachment_instance = VideoAttachment.from_json(json)
# print the JSON string representation of the object
print(VideoAttachment.to_json())

# convert the object into a dict
video_attachment_dict = video_attachment_instance.to_dict()
# create an instance of VideoAttachment from a dict
video_attachment_from_dict = VideoAttachment.from_dict(video_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


