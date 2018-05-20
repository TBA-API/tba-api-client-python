# APIStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_season** | **int** | Year of the current FRC season. | 
**max_season** | **int** | Maximum FRC season year for valid queries. | 
**is_datafeed_down** | **bool** | True if the entire FMS API provided by FIRST is down. | 
**down_events** | **list[str]** | An array of strings containing event keys of any active events that are no longer updating. | 
**ios** | [**APIStatusAppVersion**](APIStatusAppVersion.md) |  | 
**android** | [**APIStatusAppVersion**](APIStatusAppVersion.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


