# TimezonesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Timezone]**](Timezone.md) |  | 
**pages** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.timezones_response import TimezonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimezonesResponse from a JSON string
timezones_response_instance = TimezonesResponse.from_json(json)
# print the JSON string representation of the object
print(TimezonesResponse.to_json())

# convert the object into a dict
timezones_response_dict = timezones_response_instance.to_dict()
# create an instance of TimezonesResponse from a dict
timezones_response_from_dict = TimezonesResponse.from_dict(timezones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


