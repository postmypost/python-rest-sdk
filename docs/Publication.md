# Publication

Contains information about the publication, scheduled time, status, publication details, and the accounts where it is published

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Publication ID | 
**post_at** | **datetime** | The scheduled or actual date and time when the post is (or was) published | 
**delete_at** | **datetime** | The scheduled date and time for automatic deletion of the pos | [optional] 
**rubric_id** | **int** | Rubric ID | [optional] 
**account_ids** | **List[int]** | List of account IDs where the post will be published | 
**details** | [**List[PublicationDetail]**](PublicationDetail.md) | Publication details for each account or account group | 
**publication_status** | [**PublicationStatusEnum**](PublicationStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.publication import Publication

# TODO update the JSON string below
json = "{}"
# create an instance of Publication from a JSON string
publication_instance = Publication.from_json(json)
# print the JSON string representation of the object
print(Publication.to_json())

# convert the object into a dict
publication_dict = publication_instance.to_dict()
# create an instance of Publication from a dict
publication_from_dict = Publication.from_dict(publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


