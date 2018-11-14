#!/usr/bin/env python

s = raw_input()

total = ""

i = 0
t = 0

while i < len(s):
    t = s[len(s) - i - 1]
    total = total + t
    i = i + 1
print total
