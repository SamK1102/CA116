#!/usr/bin/env python

mark = input()
first = mark >= 70
second = mark >= 50 and < 70
third = mark >= 40 and < 50
fail = mark < 40

print"first:"
print"second:"
print"third:"
print"fail:"
