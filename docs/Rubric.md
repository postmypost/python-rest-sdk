# Rubric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rubric ID | 
**name** | **str** | Rubric name | 

## Example

```python
from postmypost_rest_sdk.models.rubric import Rubric

# TODO update the JSON string below
json = "{}"
# create an instance of Rubric from a JSON string
rubric_instance = Rubric.from_json(json)
# print the JSON string representation of the object
print(Rubric.to_json())

# convert the object into a dict
rubric_dict = rubric_instance.to_dict()
# create an instance of Rubric from a dict
rubric_from_dict = Rubric.from_dict(rubric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


