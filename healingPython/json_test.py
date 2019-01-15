#!python

import json
from pprint import pprint

with open('test.json') as f:
    data = json.load(f)

pprint(data)
print(data)
