#!/usr/bin/python3

for r in range(9):
    for c in range(r + 1, 10):
        if r * 10 + c < 89:
            print("{:d}{:d}".format(r, c), end=", ")
print("{:d}".format(89))
