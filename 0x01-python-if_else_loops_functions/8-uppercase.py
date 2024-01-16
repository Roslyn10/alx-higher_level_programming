#!/usr/bin/python3

def uppercase(str):
    capital = ""

    for char in str:
        if 'a' <= char <= 'z':
            upperchar = chr(ord(char) - 32)
            capital += upperchar
        else:
            capital += char
    print("{}".format(capital))
