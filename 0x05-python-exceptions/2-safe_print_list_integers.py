#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for s in range(x):
        try:
            print("{:d}".format(my_list[s]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return count
