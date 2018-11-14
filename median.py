#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()
i = 0

while i < len(a):
    j = i + 1
    p = i
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1
if len(a) % 2 == 0:
    print a[len(a) / 2]
else:
    print a[len(a) / 2]
