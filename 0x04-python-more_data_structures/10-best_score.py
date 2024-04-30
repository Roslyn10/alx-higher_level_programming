#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_int = 0
    for key, value in a_dictionary.items():
        if value > max_int:
            max_int = value
    for key, value in a_dictionary.items():
        if value == max_int:
            return key
