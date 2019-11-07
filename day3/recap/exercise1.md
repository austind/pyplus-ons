# Day 3 Recap Exercise 1

1. Using Python requests, "log in" to the nxos1 device and get an authorization token. In order to generate a token, the nxos device expects a POST to the following endpoint: `https://nxos1.lasthop.io:8443/api/aaaLogin.json`. The payload of this post should contain the following data structure:

```
{
    "aaaUser": {
        "attributes": {
            "name": "pyclass",
            "pwd": "PASSWORDHERE!"
        }
    }
}
```

2. Print the status code and token received from the API to standard out.
