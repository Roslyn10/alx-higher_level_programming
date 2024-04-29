#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_of_2 = []

    for number in my_list:
        if number % 2 == 0:
            mul_of_2.append(True)
        else:
            mul_of_2.append(False)

    return mul_of_2
