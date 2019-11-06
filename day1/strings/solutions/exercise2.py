#!/usr/bin/env python
ip_addr = input("Please enter IP address: ")

ip_addr = ip_addr.split(".")

print()
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_addr))
print()
