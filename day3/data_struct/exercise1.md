# Structured Data Exercise 1

1. Open the file "struct_data1.txt" (from this directory) in a Python script. Read this text into a python variable, and then convert the string to a JSON object. This text represents the routing table on a Cisco switch.
2. Pretty print this object to stdout so you can get a good idea what you're dealing with.
3. Print the type and length of the object. In this scenario, we know that all of the elements of this object are of the same type and length, but this is not always the case. Print the type and length of the zeroith element of the object to be sure what data types you are working with.
4. Create a new dictionary variable called "parsed_data". Iterate through the structured data, creating a key in the "parsed_data" dictionary for every network that is NOT of "protocol" "L" (local routes).
5. Add the "nexthop_if" and "nexthop_ip" values to this dictionary.
6. Pretty print your output when complete, it should look similar to this:

```
{'0.0.0.0': {'nexthop_interface': 'Vlan3967', 'nexthop_ip': '172.31.255.254'},
 '172.31.254.0': {'nexthop_interface': 'Vlan254', 'nexthop_ip': ''},
 '172.31.255.254': {'nexthop_interface': 'Vlan3967', 'nexthop_ip': ''},
 '172.31.255.5': {'nexthop_interface': 'Loopback0', 'nexthop_ip': ''}}
```
