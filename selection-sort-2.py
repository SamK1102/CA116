#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
    a.append(int(s))
    s = raw_input()

i = input()
j = i + 1
while j < len(a):
    if a[j] < a[i]:
        i = j
    j = j + 1
print i
