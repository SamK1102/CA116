#!/usr/bin/env python

a, b, c = input(), input(), input()

if a + b > c and a + c > b and b + c > a:
    print "yes"
else:
    print "no"
