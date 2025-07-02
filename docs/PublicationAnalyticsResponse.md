# PublicationAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PublicationAnalytics]**](PublicationAnalytics.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.publication_analytics_response import PublicationAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationAnalyticsResponse from a JSON string
publication_analytics_response_instance = PublicationAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicationAnalyticsResponse.to_json())

# convert the object into a dict
publication_analytics_response_dict = publication_analytics_response_instance.to_dict()
# create an instance of PublicationAnalyticsResponse from a dict
publication_analytics_response_from_dict = PublicationAnalyticsResponse.from_dict(publication_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


