# PublicationDetailEditRequest

Parameters for creating or updating publication details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | [optional] 
**publication_type** | [**PublicationDetailPublicationTypeEnum**](PublicationDetailPublicationTypeEnum.md) |  | 
**content** | **str** | Publication text | [optional] 
**comment** | **str** | First comment on the publication | [optional] 
**link** | **str** | External link for the publication | [optional] 
**title** | **str** | Publication title | [optional] 
**tiktok_comment** | **bool** | Allow comments on TikTok | [optional] 
**tiktok_duet** | **bool** | Allow duets on TikTok | [optional] 
**tiktok_stitch** | **bool** | Allow stitch on TikTok | [optional] 
**tiktok_privacy_status** | [**PublicationDetailTikTokPrivacyStatusEnum**](PublicationDetailTikTokPrivacyStatusEnum.md) |  | [optional] 
**youtube_privacy_status** | [**PublicationDetailYouTubePrivacyStatusEnum**](PublicationDetailYouTubePrivacyStatusEnum.md) |  | [optional] 
**file_ids** | **List[int]** | File IDs | [optional] 

## Example

```python
from postmypost_rest_sdk.models.publication_detail_edit_request import PublicationDetailEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationDetailEditRequest from a JSON string
publication_detail_edit_request_instance = PublicationDetailEditRequest.from_json(json)
# print the JSON string representation of the object
print(PublicationDetailEditRequest.to_json())

# convert the object into a dict
publication_detail_edit_request_dict = publication_detail_edit_request_instance.to_dict()
# create an instance of PublicationDetailEditRequest from a dict
publication_detail_edit_request_from_dict = PublicationDetailEditRequest.from_dict(publication_detail_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


