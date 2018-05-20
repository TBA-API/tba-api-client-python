# net.thefletcher.tbaapi.v3client.DistrictApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_events**](DistrictApi.md#get_district_events) | **GET** /district/{district_key}/events | 
[**get_district_events_keys**](DistrictApi.md#get_district_events_keys) | **GET** /district/{district_key}/events/keys | 
[**get_district_events_simple**](DistrictApi.md#get_district_events_simple) | **GET** /district/{district_key}/events/simple | 
[**get_district_rankings**](DistrictApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
[**get_district_teams**](DistrictApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
[**get_district_teams_keys**](DistrictApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
[**get_district_teams_simple**](DistrictApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
[**get_districts_by_year**](DistrictApi.md#get_districts_by_year) | **GET** /districts/{year} | 
[**get_event_district_points**](DistrictApi.md#get_event_district_points) | **GET** /event/{event_key}/district_points | 
[**get_team_districts**](DistrictApi.md#get_team_districts) | **GET** /team/{team_key}/districts | 


# **get_district_events**
> list[Event] get_district_events(district_key, if_modified_since=if_modified_since)



Gets a list of events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_events: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_events_keys**
> list[str] get_district_events_keys(district_key, if_modified_since=if_modified_since)



Gets a list of event keys for events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events_keys(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_events_keys: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_events_simple**
> list[EventSimple] get_district_events_simple(district_key, if_modified_since=if_modified_since)



Gets a short-form list of events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_events_simple(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_events_simple: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_rankings**
> list[DistrictRanking] get_district_rankings(district_key, if_modified_since=if_modified_since)



Gets a list of team district rankings for the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_rankings(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_rankings: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams**
> list[Team] get_district_teams(district_key, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_teams(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_teams: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams_keys**
> list[str] get_district_teams_keys(district_key, if_modified_since=if_modified_since)



Gets a list of `Team` objects that competed in events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_teams_keys(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_teams_keys: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams_simple**
> list[TeamSimple] get_district_teams_simple(district_key, if_modified_since=if_modified_since)



Gets a short-form list of `Team` objects that competed in events in the given district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
district_key = 'district_key_example' # str | TBA District Key, eg `2016fim`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_district_teams_simple(district_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_district_teams_simple: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_districts_by_year**
> list[DistrictList] get_districts_by_year(year, if_modified_since=if_modified_since)



Gets a list of districts and their corresponding district key, for the given year.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
year = 56 # int | Competition Year (or Season). Must be 4 digits.
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_districts_by_year(year, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_districts_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Competition Year (or Season). Must be 4 digits. | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[DistrictList]**](DistrictList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_district_points**
> EventDistrictPoints get_event_district_points(event_key, if_modified_since=if_modified_since)



Gets a list of team rankings for the Event.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_event_district_points(event_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_event_district_points: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_districts**
> list[DistrictList] get_team_districts(team_key, if_modified_since=if_modified_since)



Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district.

### Example
```python
from __future__ import print_function
import time
import net.thefletcher.tbaapi.v3client
from net.thefletcher.tbaapi.v3client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = net.thefletcher.tbaapi.v3client.Configuration()
configuration.api_key['X-TBA-Auth-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# create an instance of the API class
api_instance = net.thefletcher.tbaapi.v3client.DistrictApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
team_key = 'team_key_example' # str | TBA Team Key, eg `frc254`
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_team_districts(team_key, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictApi->get_team_districts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_key** | **str**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**list[DistrictList]**](DistrictList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

