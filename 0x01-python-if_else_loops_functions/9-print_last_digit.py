#!/usr/bin/python3

def print_last_digit(number):
    last_digit = str(abs(number))[-1]
    print(last_digit, end="")
    return int(last_digit)
