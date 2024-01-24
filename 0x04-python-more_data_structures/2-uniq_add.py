#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_ints = set()
    for number in my_list:
        if isinstance(number, int):
            unique_ints.add(number)

    return sum(unique_ints)
