# EventSimple

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event. | 
**name** | **str** | Official name of event on record either provided by FIRST or organizers of offseason event. | 
**event_code** | **str** | Event short code, as provided by FIRST. | 
**event_type** | **int** | Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2 | 
**district** | [**DistrictList**](DistrictList.md) | The district this event is in, may be null. | [optional] 
**city** | **str** | City, town, village, etc. the event is located in. | [optional] 
**state_prov** | **str** | State or Province the event is located in. | [optional] 
**country** | **str** | Country the event is located in. | [optional] 
**start_date** | **date** | Event start date in &#x60;yyyy-mm-dd&#x60; format. | 
**end_date** | **date** | Event end date in &#x60;yyyy-mm-dd&#x60; format. | 
**year** | **int** | Year the event data is for. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


