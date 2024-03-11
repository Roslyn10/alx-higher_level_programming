#!/usr/bin/python3

for r in range(9):
    for l in range(r + 1, 10):
        if r * 10 + l < 89:
            print("{:d}{:d}".format(r, l), end=", ")
print("{:d}".format(89))
