# Create a new directory
$ cd ~
$ mkdir MY_VENV
$ cd MY_VENV

# Exit current virtualenv
$ deactivate

# Create new virtualenv
$ python -m venv VENV

# Activate new virtualenv
$ source ~/MY_VENV/VENV/bin/activate

$ pip list
Package    Version
---------- -------
pip        19.0.1
setuptools 40.7.1
wheel      0.32.3


# Install netmiko package (and dependencies)
$ pip install netmiko
...output omitted


# List current packages
$ pip list
Package      Version
------------ -------
asn1crypto   0.24.0
bcrypt       3.1.6
cffi         1.11.5
cryptography 2.5
netmiko      2.3.0
paramiko     2.4.2
pip          19.0.1
pyasn1       0.4.5
pycparser    2.19
PyNaCl       1.3.0
pyserial     3.4
PyYAML       3.13
scp          0.13.0
setuptools   40.7.1
six          1.12.0
textfsm      0.4.1
wheel        0.32.3
