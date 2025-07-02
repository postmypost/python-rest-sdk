# UnprocessableEntityError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from postmypost_rest_sdk.models.unprocessable_entity_error import UnprocessableEntityError

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessableEntityError from a JSON string
unprocessable_entity_error_instance = UnprocessableEntityError.from_json(json)
# print the JSON string representation of the object
print(UnprocessableEntityError.to_json())

# convert the object into a dict
unprocessable_entity_error_dict = unprocessable_entity_error_instance.to_dict()
# create an instance of UnprocessableEntityError from a dict
unprocessable_entity_error_from_dict = UnprocessableEntityError.from_dict(unprocessable_entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


