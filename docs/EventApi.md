# tbaapiv3client.EventApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_events**](EventApi.md#get_district_events) | **GET** /district/{district_key}/events | 
[**get_district_events_keys**](EventApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
[**get_district_events_simple**](EventApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
[**get_event**](EventApi.md#get_event) | **GET** /event/{event_key} | 
[**get_event_alliances**](EventApi.md#get_event_alliances) | **GET** /event/{event_key}/alliances | 
[**get_event_awards**](EventApi.md#get_event_awards) | **GET** /event/{event_key}/awards | 
[**get_event_district_points**](EventApi.md#get_event_district_points) | **GET** /event/{event_key}/district_points | 
[**get_event_insights**](EventApi.md#get_event_insights) | **GET** /event/{event_key}/insights | 
[**get_event_match_timeseries**](EventApi.md#get_event_match_timeseries) | **GET** /event/{event_key}/matches/timeseries | 
[**get_event_matches**](EventApi.md#get_event_matches) | **GET** /event/{event_key}/matches | 
[**get_event_matches_keys**](EventApi.md#get_event_matches_keys) | **GET** /event/{event_key}/matches/keys | 
[**get_event_matches_simple**](EventApi.md#get_event_matches_simple) | **GET** /event/{event_key}/matches/simple | 
[**get_event_op_rs**](EventApi.md#get_event_op_rs) | **GET** /event/{event_key}/oprs | 
[**get_event_predictions**](EventApi.md#get_event_predictions) | **GET** /event/{event_key}/predictions | 
[**get_event_rankings**](EventApi.md#get_event_rankings) | **GET** /event/{event_key}/rankings | 
[**get_event_simple**](EventApi.md#get_event_simple) | **GET** /event/{event_key}/simple | 
[**get_event_teams**](EventApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
[**get_event_teams_keys**](EventApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
[**get_event_teams_simple**](EventApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
[**get_event_teams_statuses**](EventApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
[**get_events_by_year**](EventApi.md#get_events_by_year) | **GET** /events/{year} | 
[**get_events_by_year_keys**](EventApi.md#get_events_by_year_keys) | **GET** /events/{year}/keys | 
[**get_events_by_year_simple**](EventApi.md#get_events_by_year_simple) | **GET** /events/{year}/simple | 
[**get_team_event_awards**](EventApi.md#get_team_event_awards) | **GET** /team/{team_key}/event/{event_key}/awards | 
[**get_team_event_matches**](EventApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
[**get_team_event_matches_keys**](EventApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
[**get_team_event_matches_simple**](EventApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
[**get_team_event_status**](EventApi.md#get_team_event_status) | **GET** /team/{team_key}/event/{event_key}/status | 
[**get_team_events**](EventApi.md#get_team_events) | **GET** /team/{team_key}/events | 
[**get_team_events_by_year**](EventApi.md#get_team_events_by_year) | **GET** /team/{team_key}/events/{year} | 
[**get_team_events_by_year_keys**](EventApi.md#get_team_events_by_year_keys) | **GET** /team/{team_key}/events/{year}/keys | 
[**get_team_events_by_year_simple**](EventApi.md#get_team_events_by_year_simple) | **GET** /team/{team_key}/events/{year}/simple | 
[**get_team_events_keys**](EventApi.md#get_team_events_keys) | **GET** /team/{team_key}/events/keys | 
[**get_team_events_simple**](EventApi.md#get_team_events_simple) | **GET** /team/{team_key}/events/simple | 
[**get_team_events_statuses_by_year**](EventApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 


# **get_district_events**
> list[Event] get_district_events(district_key, if_modified_since=if_modified_since)



Gets a list of events in the given district.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_district_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_events_keys**
> list[str] get_district_events_keys(district_key, if_modified_since=if_modified_since)



Gets a list of event keys for events in the given district.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events_keys(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_district_events_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_events_simple**
> list[EventSimple] get_district_events_simple(district_key, if_modified_since=if_modified_since)



Gets a short-form list of events in the given district.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events_simple(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_district_events_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> Event get_event(event_key, if_modified_since=if_modified_since)



Gets an Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_alliances**
> list[EliminationAlliance] get_event_alliances(event_key, if_modified_since=if_modified_since)



Gets a list of Elimination Alliances for the given Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_alliances(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_alliances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[EliminationAlliance]**](EliminationAlliance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_awards**
> list[Award] get_event_awards(event_key, if_modified_since=if_modified_since)



Gets a list of awards from the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_awards(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_awards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_district_points**
> EventDistrictPoints get_event_district_points(event_key, if_modified_since=if_modified_since)



Gets a list of team rankings for the Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_district_points(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_district_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventDistrictPoints**](EventDistrictPoints.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_insights**
> EventInsights get_event_insights(event_key, if_modified_since=if_modified_since)



Gets a set of Event-specific insights for the given Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_insights(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventInsights**](EventInsights.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_match_timeseries**
> list[str] get_event_match_timeseries(event_key, if_modified_since=if_modified_since)



Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_match_timeseries(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_match_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_matches**
> list[Match] get_event_matches(event_key, if_modified_since=if_modified_since)



Gets a list of matches for the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_matches_keys**
> list[str] get_event_matches_keys(event_key, if_modified_since=if_modified_since)



Gets a list of match keys for the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches_keys(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_matches_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_matches_simple**
> list[MatchSimple] get_event_matches_simple(event_key, if_modified_since=if_modified_since)



Gets a short-form list of matches for the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches_simple(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_matches_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[MatchSimple]**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_op_rs**
> EventOPRs get_event_op_rs(event_key, if_modified_since=if_modified_since)



Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_op_rs(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventOPRs**](EventOPRs.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_predictions**
> object get_event_predictions(event_key, if_modified_since=if_modified_since)



Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_predictions(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_rankings**
> EventRanking get_event_rankings(event_key, if_modified_since=if_modified_since)



Gets a list of team rankings for the Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_rankings(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventRanking**](EventRanking.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_simple**
> EventSimple get_event_simple(event_key, if_modified_since=if_modified_since)



Gets a short-form Event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_simple(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventSimple**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams**
> list[Team] get_event_teams(event_key, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_teams(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_keys**
> list[str] get_event_teams_keys(event_key, if_modified_since=if_modified_since)



Gets a list of `Team` keys that competed in the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_teams_keys(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_teams_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_simple**
> list[TeamSimple] get_event_teams_simple(event_key, if_modified_since=if_modified_since)



Gets a short-form list of `Team` objects that competed in the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_teams_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_statuses**
> dict(str, TeamEventStatus) get_event_teams_statuses(event_key, if_modified_since=if_modified_since)



Gets a key-value list of the event statuses for teams competing at the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_teams_statuses(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_teams_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**dict(str, TeamEventStatus)**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_year**
> list[Event] get_events_by_year(year, if_modified_since=if_modified_since)



Gets a list of events in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_events_by_year(year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_events_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_year_keys**
> list[str] get_events_by_year_keys(year, if_modified_since=if_modified_since)



Gets a list of event keys in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_events_by_year_keys(year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_events_by_year_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_year_simple**
> list[EventSimple] get_events_by_year_simple(year, if_modified_since=if_modified_since)



Gets a short-form list of events in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_events_by_year_simple(year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_events_by_year_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_awards**
> list[Award] get_team_event_awards(team_key, event_key, if_modified_since=if_modified_since)



Gets a list of awards the given team won at the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_awards(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_event_awards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches**
> list[Match] get_team_event_matches(team_key, event_key, if_modified_since=if_modified_since)



Gets a list of matches for the given team and event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_event_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches_keys**
> list[str] get_team_event_matches_keys(team_key, event_key, if_modified_since=if_modified_since)



Gets a list of match keys for matches for the given team and event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches_keys(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_event_matches_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches_simple**
> list[Match] get_team_event_matches_simple(team_key, event_key, if_modified_since=if_modified_since)



Gets a short-form list of matches for the given team and event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches_simple(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_event_matches_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_status**
> TeamEventStatus get_team_event_status(team_key, event_key, if_modified_since=if_modified_since)



Gets the competition rank and status of the team at the given event.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_status(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_event_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **event_key** | **str**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**TeamEventStatus**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events**
> list[Event] get_team_events(team_key, if_modified_since=if_modified_since)



Gets a list of all events this team has competed at.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events(team_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year**
> list[Event] get_team_events_by_year(team_key, year, if_modified_since=if_modified_since)



Gets a list of events this team has competed at in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_by_year(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year_keys**
> list[str] get_team_events_by_year_keys(team_key, year, if_modified_since=if_modified_since)



Gets a list of the event keys for events this team has competed at in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_by_year_keys(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_by_year_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year_simple**
> list[EventSimple] get_team_events_by_year_simple(team_key, year, if_modified_since=if_modified_since)



Gets a short-form list of events this team has competed at in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_by_year_simple(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_by_year_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_keys**
> list[str] get_team_events_keys(team_key, if_modified_since=if_modified_since)



Gets a list of the event keys for all events this team has competed at.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_keys(team_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_simple**
> list[EventSimple] get_team_events_simple(team_key, if_modified_since=if_modified_since)



Gets a short-form list of all events this team has competed at.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_simple(team_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_statuses_by_year**
> dict(str, TeamEventStatus) get_team_events_statuses_by_year(team_key, year, if_modified_since=if_modified_since)



Gets a key-value list of the event statuses for events this team has competed at in the given year.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_events_statuses_by_year(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_team_events_statuses_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**dict(str, TeamEventStatus)**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * Last-Modified - Indicates the date and time the data returned was last updated. Used by clients in the &#x60;If-Modified-Since&#x60; request header. <br>  |
**304** | Not Modified - Use Local Cached Value |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

