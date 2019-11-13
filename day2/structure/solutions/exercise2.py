import json
from pprint import pprint
from netmiko import ConnectHandler

NXOS1 = {
    "host": "nxos1.lasthop.io",
    "device_type": "cisco_nxos",
    "username": "pyclass",
    "password": "88newclass",
}


def main():
    conn = ConnectHandler(**NXOS1)
    version = conn.send_command("show version | json")
    print()
    pprint(json.loads(version))
    print()


if __name__ == "__main__":
    main()
