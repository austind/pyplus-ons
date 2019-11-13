#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter router password: ")
    pynet_rtr1 = {
        "device_type": "cisco_ios_telnet",
        "ip": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**pynet_rtr1)
    print(net_connect.find_prompt())
