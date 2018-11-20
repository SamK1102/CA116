#!/usr/bin/env python

j = 0
i = 0
while i < 1:
    h = raw_input()
    k = j
    while k < len(h) and h[k] != "+":
        k = k + 1
        csv = h[j:k]
        print csv
    j = k + 1
    i = i + 1
