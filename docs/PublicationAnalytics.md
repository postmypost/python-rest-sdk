# PublicationAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Publication ID | 
**external_id** | **str** | Chanel publication ID | [optional] 
**external_url** | **str** | Chanel publication URL | 
**created_at** | **datetime** | Post creation date and time | 
**content** | **str** | Post text | [optional] 
**analytics** | **Dict[str, float]** | Metrics for the post (e.g. views, likes, comments, etc.) | 
**attaches** | [**List[Attach]**](Attach.md) | Array of attachments | 

## Example

```python
from postmypost_rest_sdk.models.publication_analytics import PublicationAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationAnalytics from a JSON string
publication_analytics_instance = PublicationAnalytics.from_json(json)
# print the JSON string representation of the object
print(PublicationAnalytics.to_json())

# convert the object into a dict
publication_analytics_dict = publication_analytics_instance.to_dict()
# create an instance of PublicationAnalytics from a dict
publication_analytics_from_dict = PublicationAnalytics.from_dict(publication_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


