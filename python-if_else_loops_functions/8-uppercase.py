#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for charc in str:
        if ord("a") <= ord(charc) <= ord("z"):
            upper_str = chr(ord(charc)-32)
        else:
            upper_str = charc
        print(upper_str, end="")
    print()
