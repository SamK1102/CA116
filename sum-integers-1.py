#!/usr/bin/env python

import sys

total = 0

num = sys.stdin.readline()
while num:
    total += int(num)
    num = sys.stdin.readline()

print total
