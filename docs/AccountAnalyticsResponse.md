# AccountAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountAnalytics]**](AccountAnalytics.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.account_analytics_response import AccountAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAnalyticsResponse from a JSON string
account_analytics_response_instance = AccountAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountAnalyticsResponse.to_json())

# convert the object into a dict
account_analytics_response_dict = account_analytics_response_instance.to_dict()
# create an instance of AccountAnalyticsResponse from a dict
account_analytics_response_from_dict = AccountAnalyticsResponse.from_dict(account_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


