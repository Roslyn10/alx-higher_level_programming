#!/usr/bin/python3
for number in range(0, 100):
    de_num = str(number).zfill(2)
    print((de_num).format(), end=", " if number < 99 else "\n")
