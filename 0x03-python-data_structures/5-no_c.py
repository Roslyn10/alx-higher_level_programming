#!/usr/bin/python3

def no_c(my_string):
    translation_table = str.maketrans('', '', 'cC')
    result_str = my_string.translate(translation_table)
    return result_str
