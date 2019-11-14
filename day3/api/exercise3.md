# API Exercise 3

1. Create a new IP address in NetBox. This IP address object should be a /32 from the 192.0.2.0/24 documentation block. Print out the status code and the returned JSON.

The HTTP headers for this request should be the same as the previous exercise.

The URL for the HTTP POST is:

https://netbox.lasthop.io/api/ipam/ip-addresses/

The JSON payload data for this request should be similar to the following:

```
data = {"address": "192.0.2.100/32"}
```

2. Using the response data from the HTTP POST that created the previous task, capture the "id" of the newly created IP address object. Using this ID, construct a new URL. Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address. Your IP address URL should be of the following form:

https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/

where `{address_id}` is the ID of the object that you just created.

Pretty print the `response.json()` data from this HTTP GET. Please note the ID of the address object that you just created.

3. Building on the script from the previous task, add a description to the the IP address object that you just created. Accomplish this using an HTTP PUT. The HTTP PUT operation will require all of the mandatory fields in the object (in this case, the "address" field). Print the status code and the response.json() from your PUT operation. The HTTP PUT operation will use same URL as exercise 4b (i.e. the URL of the newly created IP address object including its ID).

4. Finally, use an HTTP DELETE and to delete the IP address object that you just created. Remember to reference the ID of your object.
