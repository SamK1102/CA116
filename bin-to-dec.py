#!/usr/bin/env python

n = raw_input()
v = 0

i = 0
while i < len(n):
    if n[len(n) - i - 1] == "1":
        v = v + 2 ** i
    i = i + 1
print v
