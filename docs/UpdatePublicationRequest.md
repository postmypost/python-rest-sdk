# UpdatePublicationRequest

Request to update a publication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_at** | **datetime** | The scheduled or actual date and time when the post is (or was) published | 
**delete_at** | **datetime** | The scheduled date and time for automatic deletion of the pos | [optional] 
**rubric_id** | **int** | Rubric ID | [optional] 
**account_ids** | **List[int]** | List of account IDs where the publication will be posted | 
**publication_status** | [**PublicationStatusEnumEdit**](PublicationStatusEnumEdit.md) |  | 
**details** | [**List[PublicationDetailEditRequest]**](PublicationDetailEditRequest.md) | Publication details for each account or group of accounts | 

## Example

```python
from postmypost_rest_sdk.models.update_publication_request import UpdatePublicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePublicationRequest from a JSON string
update_publication_request_instance = UpdatePublicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePublicationRequest.to_json())

# convert the object into a dict
update_publication_request_dict = update_publication_request_instance.to_dict()
# create an instance of UpdatePublicationRequest from a dict
update_publication_request_from_dict = UpdatePublicationRequest.from_dict(update_publication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


