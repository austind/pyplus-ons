# Python Code Structure Exercise 2

1. Write a program that connects to the nxos1 host via netmiko and gathers the output of "show version | json".
2. Use the python-JSON library to load the returned JSON as a Python data-structure. Print out the returned data structure.
3. Write the script in such a way that nothing is executed when the module is imported, but the nxos device could be accessed as follows (after importing the script):

```
>>> import exercise2
>>> dir(exercise2)
['ConnectHandler', 'NXOS1', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'json', 'main']
>>> exercise2.NXOS1
{'host': 'nxos1.lasthop.io', 'device_type': 'cisco_nxos', 'username': 'pyclass', 'password': 'bogus'}
>>>
```

