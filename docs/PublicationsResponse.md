# PublicationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Publication]**](Publication.md) |  | 
**pages** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.publications_response import PublicationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationsResponse from a JSON string
publications_response_instance = PublicationsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicationsResponse.to_json())

# convert the object into a dict
publications_response_dict = publications_response_instance.to_dict()
# create an instance of PublicationsResponse from a dict
publications_response_from_dict = PublicationsResponse.from_dict(publications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


