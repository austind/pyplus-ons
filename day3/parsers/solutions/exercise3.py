#!/usr/bin/env python
from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler

device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
conn = ConnectHandler(**device)
output = conn.send_command("show ip route", use_textfsm=True)
pprint(output)
