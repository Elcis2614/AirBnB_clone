#!/usr/bin/python3
import re
import json
x = input().split(';')[-1]
print(x)
s = json.loads(x)
print(type(s))
print(s)
