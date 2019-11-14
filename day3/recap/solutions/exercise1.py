import os
from getpass import getpass
import json
import requests

PASSWORD = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


def main():
    url = "https://nxos1.lasthop.io:8443/api/aaaLogin.json"
    payload = {"aaaUser": {"attributes": {"name": "pyclass", "pwd": PASSWORD}}}
    r = requests.post(url=url, data=json.dumps(payload), verify=False)
    print(r.status_code)
    r = r.json()
    print(r["imdata"][0]["aaaLogin"]["attributes"]["token"])


if __name__ == "__main__":
    main()
