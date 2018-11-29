#!/usr/bin/env python

employees = []

line = raw_input()
while line != "end":
    employees.append(line)
    line = raw_input()

line = raw_input()
while line != "end":
    i = 0
    while i < len(employees) and employees[i][:8] != line:
        i += 1

    if i < len(employees):
        print employees[i][9:]

    line = raw_input()
