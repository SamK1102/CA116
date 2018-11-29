#!/usr/bin/env python

a, b, c = input(), input(), input()

print a * ((c + 1) % 2) + b * (c % 2)
