#!/usr/bin/env python

import sys

f = dict()

line = sys.stdin.readline()[:-1]
while line:
    if line not in f:
        f[line] = 0

    f[line] += 1
    line = sys.stdin.readline()[:-1]

for k in f:
    if f[k] == 1:
        print k
