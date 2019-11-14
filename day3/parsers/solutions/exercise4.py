#!/usr/bin/env python
import os
from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler

password = os.getenv('PYNET_PASSWORD') if os.getenv('PYNET_PASSWORD') else getpass()
device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}
conn = ConnectHandler(**device)
output = conn.send_command("show mac address-table", use_genie=True)
pprint(output)
