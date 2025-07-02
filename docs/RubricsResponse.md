# RubricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Rubric]**](Rubric.md) |  | 
**pages** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.rubrics_response import RubricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RubricsResponse from a JSON string
rubrics_response_instance = RubricsResponse.from_json(json)
# print the JSON string representation of the object
print(RubricsResponse.to_json())

# convert the object into a dict
rubrics_response_dict = rubrics_response_instance.to_dict()
# create an instance of RubricsResponse from a dict
rubrics_response_from_dict = RubricsResponse.from_dict(rubrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


