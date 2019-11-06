#!/usr/bin/env python
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)


if __name__ == "__main__":
    filename = "exercise2.yaml"
    pprint(read_yaml(filename))
