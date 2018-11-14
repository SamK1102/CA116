#!/usr/bin/env python

i = 0
stop = False
s = raw_input()
while i < len(s) - 1 and stop is False:
    if s[i] == s[i + 1]:
        print s[i] + s[i + 1]
        stop = True
    i += 1
