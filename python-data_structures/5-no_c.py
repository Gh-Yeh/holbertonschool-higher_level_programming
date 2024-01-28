#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_str += elements
    return new_str
