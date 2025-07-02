# PublicationFileResponseEnum

Object representing a file attached to a publication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID | [optional] 
**original** | **str** | File URL | [optional] 

## Example

```python
from postmypost_rest_sdk.models.publication_file_response_enum import PublicationFileResponseEnum

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationFileResponseEnum from a JSON string
publication_file_response_enum_instance = PublicationFileResponseEnum.from_json(json)
# print the JSON string representation of the object
print(PublicationFileResponseEnum.to_json())

# convert the object into a dict
publication_file_response_enum_dict = publication_file_response_enum_instance.to_dict()
# create an instance of PublicationFileResponseEnum from a dict
publication_file_response_enum_from_dict = PublicationFileResponseEnum.from_dict(publication_file_response_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


