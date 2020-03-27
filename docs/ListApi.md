# tbaapiv3client.ListApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_events**](ListApi.md#get_district_events) | **GET** /district/{district_key}/events | 
[**get_district_events_keys**](ListApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
[**get_district_events_simple**](ListApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
[**get_district_rankings**](ListApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
[**get_district_teams**](ListApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
[**get_district_teams_keys**](ListApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
[**get_district_teams_simple**](ListApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
[**get_event_teams**](ListApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
[**get_event_teams_keys**](ListApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
[**get_event_teams_simple**](ListApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
[**get_event_teams_statuses**](ListApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
[**get_events_by_year**](ListApi.md#get_events_by_year) | **GET** /events/{year} | 
[**get_events_by_year_keys**](ListApi.md#get_events_by_year_keys) | **GET** /events/{year}/keys | 
[**get_events_by_year_simple**](ListApi.md#get_events_by_year_simple) | **GET** /events/{year}/simple | 
[**get_team_events_statuses_by_year**](ListApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 
[**get_teams**](ListApi.md#get_teams) | **GET** /teams/{page_num} | 
[**get_teams_by_year**](ListApi.md#get_teams_by_year) | **GET** /teams/{year}/{page_num} | 
[**get_teams_by_year_keys**](ListApi.md#get_teams_by_year_keys) | **GET** /teams/{year}/{page_num}/keys | 
[**get_teams_by_year_simple**](ListApi.md#get_teams_by_year_simple) | **GET** /teams/{year}/{page_num}/simple | 
[**get_teams_keys**](ListApi.md#get_teams_keys) | **GET** /teams/{page_num}/keys | 
[**get_teams_simple**](ListApi.md#get_teams_simple) | **GET** /teams/{page_num}/simple | 


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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_events(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_events: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_events_keys(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_events_keys: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_events_simple(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_events_simple: %s\n" % e)
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

# **get_district_rankings**
> list[DistrictRanking] get_district_rankings(district_key, if_modified_since=if_modified_since)



Gets a list of team district rankings for the given district.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_rankings(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[DistrictRanking]**](DistrictRanking.md)

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

# **get_district_teams**
> list[Team] get_district_teams(district_key, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in events in the given district.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_teams(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
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

# **get_district_teams_keys**
> list[str] get_district_teams_keys(district_key, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in events in the given district.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_teams_keys(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_teams_keys: %s\n" % e)
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

# **get_district_teams_simple**
> list[TeamSimple] get_district_teams_simple(district_key, if_modified_since=if_modified_since)



Gets a short-form list of `Team` objects that competed in events in the given district.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_district_teams_simple(district_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_district_teams_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_key** | **str**| TBA District Key, eg &#x60;2016fim&#x60; | 
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_event_teams(event_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_event_teams: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_event_teams_keys(event_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_event_teams_keys: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_event_teams_simple: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_event_teams_statuses(event_key, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_event_teams_statuses: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_events_by_year(year, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_events_by_year: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_events_by_year_keys(year, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_events_by_year_keys: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_events_by_year_simple(year, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_events_by_year_simple: %s\n" % e)
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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_team_events_statuses_by_year(team_key, year, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_team_events_statuses_by_year: %s\n" % e)
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

# **get_teams**
> list[Team] get_teams(page_num, if_modified_since=if_modified_since)



Gets a list of `Team` objects, paginated in groups of 500.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams(page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

# **get_teams_by_year**
> list[Team] get_teams_by_year(year, page_num, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in the given year, paginated in groups of 500.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams_by_year(year, page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

# **get_teams_by_year_keys**
> list[str] get_teams_by_year_keys(year, page_num, if_modified_since=if_modified_since)



Gets a list Team Keys that competed in the given year, paginated in groups of 500.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams_by_year_keys(year, page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams_by_year_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

# **get_teams_by_year_simple**
> list[TeamSimple] get_teams_by_year_simple(year, page_num, if_modified_since=if_modified_since)



Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups of 500.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    year = 56 # int | Competition Year (or Season). Must be 4 digits.
page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams_by_year_simple(year, page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams_by_year_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

# **get_teams_keys**
> list[str] get_teams_keys(page_num, if_modified_since=if_modified_since)



Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams_keys(page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

# **get_teams_simple**
> list[TeamSimple] get_teams_simple(page_num, if_modified_since=if_modified_since)



Gets a list of short form `Team_Simple` objects, paginated in groups of 500.

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

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.ListApi(api_client)
    page_num = 56 # int | Page number of results to return, zero-indexed
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_teams_simple(page_num, if_modified_since=if_modified_since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListApi->get_teams_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_num** | **int**| Page number of results to return, zero-indexed | 
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

