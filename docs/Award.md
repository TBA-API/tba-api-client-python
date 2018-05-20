# Award

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the award as provided by FIRST. May vary for the same award type. | 
**award_type** | **int** | Type of award given. See https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/award_type.py#L6 | 
**event_key** | **str** | The event_key of the event the award was won at. | 
**recipient_list** | [**list[AwardRecipient]**](AwardRecipient.md) | A list of recipients of the award at the event. Either team_key and/or awardee for individual awards. | 
**year** | **int** | The year this award was won. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


