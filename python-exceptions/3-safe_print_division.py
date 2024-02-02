#!/usr/bin/python3
def safe_print_division(a, b):
    divd = 0
    try:
        divd = a/b
    except ZeroDivisionError:
        divd = None
    finally:
        print("Inside result: {}".format(divd))
        return divd
