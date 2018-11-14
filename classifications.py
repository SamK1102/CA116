#!/usr/bin/env python

mark = input()
first = mark >= 70
second = mark >= 50 and < 69
third = mark >= 40 and < 49
fail = mark < 39

print"first:"
print"second:"
print"third:"
print"fail:"
