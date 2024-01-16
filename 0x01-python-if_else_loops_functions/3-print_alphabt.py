#!/usr/bin/python3
for ac in range(97, 123):
    if chr(ac) not in ['e', 'q']:
        print(chr(ac).format(), end="")
