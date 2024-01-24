#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    my_list = initial list
    search = element to replace
    replace = new element
    """
    new_list = [replace if y == search else y for y in my_list]
    return new_list
