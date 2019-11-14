# API Exercise 4

1. Using the response data from the HTTP POST that created the previous task, capture the "id" of the newly created IP address object. Using this ID, construct a new URL. Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address. Your IP address URL should be of the following form:

https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/

where `{address_id}` is the ID of the object that you just created.

Pretty print the `response.json()` data from this HTTP GET. Please note the ID of the address object that you just created.

2. Building on the script from the previous task, add a description to the the IP address object that you just created. Accomplish this using an HTTP PUT. The HTTP PUT operation will require all of the mandatory fields in the object (in this case, the "address" field). Print the status code and the response.json() from your PUT operation. The HTTP PUT operation will use same URL as exercise 4b (i.e. the URL of the newly created IP address object including its ID).

3. Finally, use an HTTP DELETE and to delete the IP address object that you just created. Remember to reference the ID of your object.
