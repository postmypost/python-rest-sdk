# NotFoundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **int** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from postmypost_rest_sdk.models.not_found_error import NotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundError from a JSON string
not_found_error_instance = NotFoundError.from_json(json)
# print the JSON string representation of the object
print(NotFoundError.to_json())

# convert the object into a dict
not_found_error_dict = not_found_error_instance.to_dict()
# create an instance of NotFoundError from a dict
not_found_error_from_dict = NotFoundError.from_dict(not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


