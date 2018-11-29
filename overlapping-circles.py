#!/usr/bin/env python

x1, y1, r1, x2, y2, r2 = input(), input(), input(), input(), input(), input()

if (x2 - x1) ** 2 + (y2 - y1) ** 2 < (r1 + r2) ** 2:
    print "yes"
else:
    print "no"
