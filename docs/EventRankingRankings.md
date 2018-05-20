# EventRankingRankings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dq** | **int** | Number of times disqualified. | 
**matches_played** | **int** | Number of matches played by this team. | 
**qual_average** | **int** | The average match score during qualifications. Year specific. May be null if not relevant for a given year. | [optional] 
**rank** | **int** | The team&#39;s rank at the event as provided by FIRST. | 
**record** | [**WLTRecord**](WLTRecord.md) |  | 
**extra_stats** | **list[float]** | Additional special data on the team&#39;s performance calculated by TBA. | [optional] 
**sort_orders** | **list[float]** | Additional year-specific information, may be null. See parent &#x60;sort_order_info&#x60; for details. | [optional] 
**team_key** | **str** | The team with this rank. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


