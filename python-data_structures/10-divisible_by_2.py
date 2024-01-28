#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = [bool(number % 2 == 0) for number in my_list]
    return new_list
