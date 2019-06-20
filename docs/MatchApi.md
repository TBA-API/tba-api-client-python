# tbaapiv3client.MatchApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_match_timeseries**](MatchApi.md#get_event_match_timeseries) | **GET** /event/{event_key}/matches/timeseries | 
[**get_event_matches**](MatchApi.md#get_event_matches) | **GET** /event/{event_key}/matches | 
[**get_event_matches_keys**](MatchApi.md#get_event_matches_keys) | **GET** /event/{event_key}/matches/keys | 
[**get_event_matches_simple**](MatchApi.md#get_event_matches_simple) | **GET** /event/{event_key}/matches/simple | 
[**get_match**](MatchApi.md#get_match) | **GET** /match/{match_key} | 
[**get_match_simple**](MatchApi.md#get_match_simple) | **GET** /match/{match_key}/simple | 
[**get_match_timeseries**](MatchApi.md#get_match_timeseries) | **GET** /match/{match_key}/timeseries | 
[**get_team_event_matches**](MatchApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
[**get_team_event_matches_keys**](MatchApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
[**get_team_event_matches_simple**](MatchApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
[**get_team_matches_by_year**](MatchApi.md#get_team_matches_by_year) | **GET** /team/{team_key}/matches/{year} | 
[**get_team_matches_by_year_keys**](MatchApi.md#get_team_matches_by_year_keys) | **GET** /team/{team_key}/matches/{year}/keys | 
[**get_team_matches_by_year_simple**](MatchApi.md#get_team_matches_by_year_simple) | **GET** /team/{team_key}/matches/{year}/simple | 


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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_match_timeseries(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_event_match_timeseries: %s\n" % e)
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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches_keys(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_event_matches_keys: %s\n" % e)
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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_matches_simple(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_event_matches_simple: %s\n" % e)
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

# **get_match**
> Match get_match(match_key, if_modified_since=if_modified_since)



Gets a `Match` object for the given match key.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
match_key = 'match_key_example' # str | TBA Match Key, eg `2016nytr_qm1`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_match(match_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_key** | **str**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**Match**](Match.md)

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

# **get_match_simple**
> MatchSimple get_match_simple(match_key, if_modified_since=if_modified_since)



Gets a short-form `Match` object for the given match key.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
match_key = 'match_key_example' # str | TBA Match Key, eg `2016nytr_qm1`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_match_simple(match_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_match_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_key** | **str**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**MatchSimple**](MatchSimple.md)

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

# **get_match_timeseries**
> list[object] get_match_timeseries(match_key, if_modified_since=if_modified_since)



Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if not available. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
match_key = 'match_key_example' # str | TBA Match Key, eg `2016nytr_qm1`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_match_timeseries(match_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_match_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_key** | **str**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**list[object]**

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_event_matches: %s\n" % e)
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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches_keys(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_event_matches_keys: %s\n" % e)
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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_event_matches_simple(team_key, event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_event_matches_simple: %s\n" % e)
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

# **get_team_matches_by_year**
> list[Match] get_team_matches_by_year(team_key, year, if_modified_since=if_modified_since)



Gets a list of matches for the given team and year.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_matches_by_year(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_matches_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
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

# **get_team_matches_by_year_keys**
> list[str] get_team_matches_by_year_keys(team_key, year, if_modified_since=if_modified_since)



Gets a list of match keys for matches for the given team and year.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_matches_by_year_keys(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_matches_by_year_keys: %s\n" % e)
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

# **get_team_matches_by_year_simple**
> list[MatchSimple] get_team_matches_by_year_simple(team_key, year, if_modified_since=if_modified_since)



Gets a short-form list of matches for the given team and year.

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

# create an instance of the API class
api_instance = tbaapiv3client.MatchApi(tbaapiv3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_matches_by_year_simple(team_key, year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->get_team_matches_by_year_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
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

