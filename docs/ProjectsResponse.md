# ProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Project]**](Project.md) |  | 
**pages** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from postmypost_rest_sdk.models.projects_response import ProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsResponse from a JSON string
projects_response_instance = ProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectsResponse.to_json())

# convert the object into a dict
projects_response_dict = projects_response_instance.to_dict()
# create an instance of ProjectsResponse from a dict
projects_response_from_dict = ProjectsResponse.from_dict(projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


