#!/usr/bin/env python
from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
conn = ConnectHandler(**device)
output = conn.send_command("show mac address-table", use_genie=True)
pprint(output)
