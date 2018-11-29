#!/usr/bin/env python

import sys

n = 13
lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper = "abcdefghijklmnopqrstuvwxyz"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

d = {
}

i = 0
while i < len(src):
    d[src[i]] = dst[i]
    i = i + 1

f = sys.stdin.read().strip()
s = []
i = 0
while i < len(f):
    if f[i] not in src:
        s.append(f[i])
    else:
        s.append(d[f[i]])
    i = i + 1
print "".join(s)
