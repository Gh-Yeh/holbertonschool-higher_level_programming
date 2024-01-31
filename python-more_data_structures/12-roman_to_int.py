#!/usr/bin/python
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    number = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for index, chr in enumerate(roman_string):
        if chr == "I" and index < len(roman_string)-1:
            if roman_string[index+1] == 'V':
                number += 4
                roman_string = roman_string.replace("IV", "--")
            if roman_string[index+1] == 'X':
                number += 9
                roman_string = roman_string.replace("IX", "--")
        if chr in roman:
            number += (roman[chr] * roman_string.count(chr))
            roman_string = roman_string.replace(chr, "-")
    return number
