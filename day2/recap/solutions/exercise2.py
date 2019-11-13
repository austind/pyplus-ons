#!/usr/bin/env python
from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
conn = ConnectHandler(**device)
output = conn.send_command("show ip int brief")

ip_dict = {}
for line in output.splitlines():
    line = line.strip()
    if "Interface" in line:
        continue
    elif "administratively down" in line:
        interface, ip_address, _, _, status1, status2, protocol = line.split()
        status = f"{status1}_{status2}"
    else:
        interface, ip_address, _, _, status, protocol = line.split()
    fields = {"ip_address": ip_address, "line_status": status, "line_protocol": protocol}
    ip_dict[interface] = fields


pprint(ip_dict)
