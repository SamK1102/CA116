#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][-3:] == ".py":
        with open(files[i]) as f:
            if f.readlines():
                print files[i]
    i = i + 1
