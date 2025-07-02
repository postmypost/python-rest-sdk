# PublicationDetail

Publication details for a specific account or platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | [optional] 
**content** | **str** | Publication text | [optional] 
**comment** | **str** | First comment | [optional] 
**link** | **str** | External link for the publication | [optional] 
**title** | **str** | Publication title | [optional] 
**tiktok_comment** | **bool** | Allow comments on TikTok | [optional] 
**tiktok_duet** | **bool** | Allow duets on TikTok | [optional] 
**tiktok_stitch** | **bool** | Allow stitch on TikTok | [optional] 
**tiktok_privacy_status** | [**PublicationDetailTikTokPrivacyStatusEnum**](PublicationDetailTikTokPrivacyStatusEnum.md) |  | [optional] 
**files** | [**List[PublicationFileResponseEnum]**](PublicationFileResponseEnum.md) | List of files attached to the publication | [optional] 
**publication_type** | [**PublicationDetailPublicationTypeEnum**](PublicationDetailPublicationTypeEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.publication_detail import PublicationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationDetail from a JSON string
publication_detail_instance = PublicationDetail.from_json(json)
# print the JSON string representation of the object
print(PublicationDetail.to_json())

# convert the object into a dict
publication_detail_dict = publication_detail_instance.to_dict()
# create an instance of PublicationDetail from a dict
publication_detail_from_dict = PublicationDetail.from_dict(publication_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


