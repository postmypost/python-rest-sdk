# Timezone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timezone ID | 
**name** | **str** | Timezone name | 
**utc_offset** | **float** | Offset relative to UTC+0 | 

## Example

```python
from postmypost_rest_sdk.models.timezone import Timezone

# TODO update the JSON string below
json = "{}"
# create an instance of Timezone from a JSON string
timezone_instance = Timezone.from_json(json)
# print the JSON string representation of the object
print(Timezone.to_json())

# convert the object into a dict
timezone_dict = timezone_instance.to_dict()
# create an instance of Timezone from a dict
timezone_from_dict = Timezone.from_dict(timezone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


