#!/usr/bin/python3
for alph in range(ord('a'), ord('z')+1):
    if (chr(alph) == "q" or chr(alph) == "e"):
        continue
    print(chr(alph), end='')
