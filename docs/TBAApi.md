# net.thefletcher.tbaapi.v3client.TBAApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](TBAApi.md#get_status) | **GET** /status | 


# **get_status**
> APIStatus get_status(if_modified_since=if_modified_since)



Returns API status, and TBA status information.

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
api_instance = net.thefletcher.tbaapi.v3client.TBAApi(net.thefletcher.tbaapi.v3client.ApiClient(configuration))
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_status(if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TBAApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **str**| Value of the &#x60;Last-Modified&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**APIStatus**](APIStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

