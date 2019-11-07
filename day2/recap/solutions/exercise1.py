#!/usr/bin/env python
from pprint import pprint

with open("exercise1.txt") as f:
    output = f.readlines()

ip_dict = {}
for line in output:
    line = line.strip()
    if "Interface" in line:
        continue
    interface, ip_address, _, _, status, protocol = line.split()
    fields = {
        "ip_address": ip_address,
        "line_status": status,
        "line_protocol": protocol,
    }
    ip_dict[interface] = fields


pprint(ip_dict)
