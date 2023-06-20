#!/usr/bin/python3
import re

def f(txt):
    s = "^[A-Za-z]*\.[a-z]*\(\".*\"\)$"
    x = re.search(s,txt)
    if (x):
        print("Found")
s = input()
f(s)
