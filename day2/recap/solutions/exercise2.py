#!/usr/bin/env python
from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
conn = ConnectHandler(**cisco1)
output = conn.send_command("show ip int brief")

ip_dict = {}
for line in output:
    line = line.strip()
    if "Interface" in line:
        continue
    interface, ip_address, _, _, status, protocol = line.split()
    fields = {"ip_address": ip_address, "line_status": status, "line_protocol": protocol}
    ip_dict[interface] = fields


pprint(ip_dict)
