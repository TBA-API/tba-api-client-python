# tbaapiv3client.TeamApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_rankings**](TeamApi.md#get_district_rankings) | **GET** /district/{district_key}/rankings | 
[**get_district_teams**](TeamApi.md#get_district_teams) | **GET** /district/{district_key}/teams | 
[**get_district_teams_keys**](TeamApi.md#get_district_teams_keys) | **GET** /district/{district_key}/teams/keys | 
[**get_district_teams_simple**](TeamApi.md#get_district_teams_simple) | **GET** /district/{district_key}/teams/simple | 
[**get_event_teams**](TeamApi.md#get_event_teams) | **GET** /event/{event_key}/teams | 
[**get_event_teams_keys**](TeamApi.md#get_event_teams_keys) | **GET** /event/{event_key}/teams/keys | 
[**get_event_teams_simple**](TeamApi.md#get_event_teams_simple) | **GET** /event/{event_key}/teams/simple | 
[**get_event_teams_statuses**](TeamApi.md#get_event_teams_statuses) | **GET** /event/{event_key}/teams/statuses | 
[**get_team**](TeamApi.md#get_team) | **GET** /team/{team_key} | 
[**get_team_awards**](TeamApi.md#get_team_awards) | **GET** /team/{team_key}/awards | 
[**get_team_awards_by_year**](TeamApi.md#get_team_awards_by_year) | **GET** /team/{team_key}/awards/{year} | 
[**get_team_districts**](TeamApi.md#get_team_districts) | **GET** /team/{team_key}/districts | 
[**get_team_event_awards**](TeamApi.md#get_team_event_awards) | **GET** /team/{team_key}/event/{event_key}/awards | 
[**get_team_event_matches**](TeamApi.md#get_team_event_matches) | **GET** /team/{team_key}/event/{event_key}/matches | 
[**get_team_event_matches_keys**](TeamApi.md#get_team_event_matches_keys) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
[**get_team_event_matches_simple**](TeamApi.md#get_team_event_matches_simple) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
[**get_team_event_status**](TeamApi.md#get_team_event_status) | **GET** /team/{team_key}/event/{event_key}/status | 
[**get_team_events**](TeamApi.md#get_team_events) | **GET** /team/{team_key}/events | 
[**get_team_events_by_year**](TeamApi.md#get_team_events_by_year) | **GET** /team/{team_key}/events/{year} | 
[**get_team_events_by_year_keys**](TeamApi.md#get_team_events_by_year_keys) | **GET** /team/{team_key}/events/{year}/keys | 
[**get_team_events_by_year_simple**](TeamApi.md#get_team_events_by_year_simple) | **GET** /team/{team_key}/events/{year}/simple | 
[**get_team_events_keys**](TeamApi.md#get_team_events_keys) | **GET** /team/{team_key}/events/keys | 
[**get_team_events_simple**](TeamApi.md#get_team_events_simple) | **GET** /team/{team_key}/events/simple | 
[**get_team_events_statuses_by_year**](TeamApi.md#get_team_events_statuses_by_year) | **GET** /team/{team_key}/events/{year}/statuses | 
[**get_team_matches_by_year**](TeamApi.md#get_team_matches_by_year) | **GET** /team/{team_key}/matches/{year} | 
[**get_team_matches_by_year_keys**](TeamApi.md#get_team_matches_by_year_keys) | **GET** /team/{team_key}/matches/{year}/keys | 
[**get_team_matches_by_year_simple**](TeamApi.md#get_team_matches_by_year_simple) | **GET** /team/{team_key}/matches/{year}/simple | 
[**get_team_media_by_tag**](TeamApi.md#get_team_media_by_tag) | **GET** /team/{team_key}/media/tag/{media_tag} | 
[**get_team_media_by_tag_year**](TeamApi.md#get_team_media_by_tag_year) | **GET** /team/{team_key}/media/tag/{media_tag}/{year} | 
[**get_team_media_by_year**](TeamApi.md#get_team_media_by_year) | **GET** /team/{team_key}/media/{year} | 
[**get_team_robots**](TeamApi.md#get_team_robots) | **GET** /team/{team_key}/robots | 
[**get_team_simple**](TeamApi.md#get_team_simple) | **GET** /team/{team_key}/simple | 
[**get_team_social_media**](TeamApi.md#get_team_social_media) | **GET** /team/{team_key}/social_media | 
[**get_team_years_participated**](TeamApi.md#get_team_years_participated) | **GET** /team/{team_key}/years_participated | 
[**get_teams**](TeamApi.md#get_teams) | **GET** /teams/{page_num} | 
[**get_teams_by_year**](TeamApi.md#get_teams_by_year) | **GET** /teams/{year}/{page_num} | 
[**get_teams_by_year_keys**](TeamApi.md#get_teams_by_year_keys) | **GET** /teams/{year}/{page_num}/keys | 
[**get_teams_by_year_simple**](TeamApi.md#get_teams_by_year_simple) | **GET** /teams/{year}/{page_num}/simple | 
[**get_teams_keys**](TeamApi.md#get_teams_keys) | **GET** /teams/{page_num}/keys | 
[**get_teams_simple**](TeamApi.md#get_teams_simple) | **GET** /teams/{page_num}/simple | 


# **get_district_rankings**
> list[DistrictRanking] get_district_rankings()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_district_rankings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_district_rankings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DistrictRanking]**](DistrictRanking.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams**
> list[Team] get_district_teams()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_district_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_district_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams_keys**
> list[str] get_district_teams_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_district_teams_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_district_teams_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_teams_simple**
> list[TeamSimple] get_district_teams_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_district_teams_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_district_teams_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams**
> list[Team] get_event_teams()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_event_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_event_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_keys**
> list[str] get_event_teams_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_event_teams_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_event_teams_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_simple**
> list[TeamSimple] get_event_teams_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_event_teams_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_event_teams_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_teams_statuses**
> dict(str, TeamEventStatus) get_event_teams_statuses()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_event_teams_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_event_teams_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, TeamEventStatus)**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> Team get_team()



Gets a `Team` object for the team referenced by the given key.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Team**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_awards**
> list[Award] get_team_awards()



Gets a list of awards the given team has won.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_awards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_awards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_awards_by_year**
> list[Award] get_team_awards_by_year()



Gets a list of awards the given team has won in a given year.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_awards_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_awards_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_districts**
> list[DistrictList] get_team_districts()



Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_districts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_districts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DistrictList]**](DistrictList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_awards**
> list[Award] get_team_event_awards()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_event_awards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_event_awards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches**
> list[Match] get_team_event_matches()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_event_matches()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_event_matches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches_keys**
> list[str] get_team_event_matches_keys()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_event_matches_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_event_matches_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_matches_simple**
> list[Match] get_team_event_matches_simple()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_event_matches_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_event_matches_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_event_status**
> TeamEventStatus get_team_event_status()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_event_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_event_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamEventStatus**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events**
> list[Event] get_team_events()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year**
> list[Event] get_team_events_by_year()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year_keys**
> list[str] get_team_events_by_year_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_by_year_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_by_year_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_by_year_simple**
> list[EventSimple] get_team_events_by_year_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_by_year_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_by_year_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_keys**
> list[str] get_team_events_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_simple**
> list[EventSimple] get_team_events_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_events_statuses_by_year**
> dict(str, TeamEventStatus) get_team_events_statuses_by_year()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_events_statuses_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_events_statuses_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, TeamEventStatus)**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_matches_by_year**
> list[Match] get_team_matches_by_year()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_matches_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_matches_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_matches_by_year_keys**
> list[str] get_team_matches_by_year_keys()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_matches_by_year_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_matches_by_year_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_matches_by_year_simple**
> list[MatchSimple] get_team_matches_by_year_simple()



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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_matches_by_year_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_matches_by_year_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MatchSimple]**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_media_by_tag**
> list[Media] get_team_media_by_tag()



Gets a list of Media (videos / pictures) for the given team and tag.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_media_by_tag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_media_by_tag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Media]**](Media.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_media_by_tag_year**
> list[Media] get_team_media_by_tag_year()



Gets a list of Media (videos / pictures) for the given team, tag and year.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_media_by_tag_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_media_by_tag_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Media]**](Media.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_media_by_year**
> list[Media] get_team_media_by_year()



Gets a list of Media (videos / pictures) for the given team and year.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_media_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_media_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Media]**](Media.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_robots**
> list[TeamRobot] get_team_robots()



Gets a list of year and robot name pairs for each year that a robot name was provided. Will return an empty array if the team has never named a robot.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_robots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_robots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamRobot]**](TeamRobot.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_simple**
> TeamSimple get_team_simple()



Gets a `Team_Simple` object for the team referenced by the given key.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamSimple**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_social_media**
> list[Media] get_team_social_media()



Gets a list of Media (social media) for the given team.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_social_media()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_social_media: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Media]**](Media.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_years_participated**
> list[int] get_team_years_participated()



Gets a list of years in which the team participated in at least one competition.

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
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_team_years_participated()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_team_years_participated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> list[Team] get_teams()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_year**
> list[Team] get_teams_by_year()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams_by_year()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams_by_year: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_year_keys**
> list[str] get_teams_by_year_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams_by_year_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams_by_year_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_year_simple**
> list[TeamSimple] get_teams_by_year_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams_by_year_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams_by_year_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_keys**
> list[str] get_teams_keys()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_simple**
> list[TeamSimple] get_teams_simple()



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

# create an instance of the API class
api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->get_teams_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

