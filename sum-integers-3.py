#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):
    with open(sys.argv[i]) as f:
        num = f.readline()
        while num:
            total += int(num)
            num = f.readline()

    i += 1

print total
