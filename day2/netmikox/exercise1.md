# Netmiko Exercise 1

Write a Netmiko script that connects to one Cisco router and one Juniper SRX.

1. Print the current prompt.
2. use send_command to retrieve 'show version' from the two devices.
3. use send_command to retrieve running configuration from the two devices.
4. Save the running config to a file.

Dictionary for network devices that can be used with Netmiko.

```
cisco3 = {
    'device_type': 'cisco_ios',
    'host':   'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
}

srx2 = {
    'device_type': 'juniper_junos',
    'host':   'srx2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
}
```
