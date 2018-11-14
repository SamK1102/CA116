#!/usr/bin/env python

if __name__ == "__main__":
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a):
    if 5 < len(a[i]):
        print a[i]
    i = i + 1
