#!/usr/bin/env python

s = raw_input()
while s != 'end':
    city = ''
    state = ''
    i = 0
    pos = 0
    while i < len(s):
        if s[i] == ',' and city == '':
            city = s[pos:i]
            pos = i
        elif s[i] == ',' and state == '':
            state = s[pos + 1:i]
            pos = i
        i += 1
    if state == 'WI':
        print city
    s = raw_input()
