# Team

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | TBA team key with the format &#x60;frcXXXX&#x60; with &#x60;XXXX&#x60; representing the team number. | 
**team_number** | **int** | Official team number issued by FIRST. | 
**nickname** | **str** | Team nickname provided by FIRST. | [optional] 
**name** | **str** | Official long name registered with FIRST. | 
**city** | **str** | City of team derived from parsing the address registered with FIRST. | [optional] 
**state_prov** | **str** | State of team derived from parsing the address registered with FIRST. | [optional] 
**country** | **str** | Country of team derived from parsing the address registered with FIRST. | [optional] 
**address** | **str** | Will be NULL, for future development. | [optional] 
**postal_code** | **str** | Postal code from the team address. | [optional] 
**gmaps_place_id** | **str** | Will be NULL, for future development. | [optional] 
**gmaps_url** | **str** | Will be NULL, for future development. | [optional] 
**lat** | **float** | Will be NULL, for future development. | [optional] 
**lng** | **float** | Will be NULL, for future development. | [optional] 
**location_name** | **str** | Will be NULL, for future development. | [optional] 
**website** | **str** | Official website associated with the team. | [optional] 
**rookie_year** | **int** | First year the team officially competed. | 
**motto** | **str** | Team&#39;s motto as provided by FIRST. | [optional] 
**home_championship** | **object** | Location of the team&#39;s home championship each year as a key-value pair. The year (as a string) is the key, and the city is the value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


