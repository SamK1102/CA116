#!/usr/bin/env python

import sys
pattern = sys.argv[1]

a = []

s = raw_input()
while s != "end":
    i = 0
    a.append(s)
    s = raw_input()
    i = i + 1

j = 0
while j < len(a) and a[j] != pattern:
    j = j + 1

print a[j]
