#!/usr/bin/python3

for index, char_code in enumerate(reversed(range(ord('a'), ord('z') + 1))):
    char = chr(char_code)
    print("{}".format(char.upper() if index % 2 != 0 else char), end="")
