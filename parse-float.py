#!/usr/bin/env python
n = input()

i = 0
while i < len(n) and n[i] != ".":
    i = i + 1

print n[:i]
print n[i + 1:]
