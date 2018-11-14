#!/usr/bin/env python

x = raw_input()
y = raw_input()
z = raw_input()

if len(x) > len(y) and len(x) > len(z):
    print x
elif len(y) > len(x) and len(y) > len(z):
    print y
elif len(z) > len(x) and len(z) > len(y):
    print z
