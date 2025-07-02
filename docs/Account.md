# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account ID | 
**chanel_id** | **int** | Channel ID | 
**external_id** | **str** | Account ID in the channel | 
**name** | **str** | Account name | 
**login** | **str** | Account login | [optional] 
**connection_status** | [**AccountConnectionStatusEnum**](AccountConnectionStatusEnum.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


