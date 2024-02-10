#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    for delim in special_chars:
        text = (delim + ("\n" * 2)).join([sentence.strip(" ")
                                          for sentence in text.split(delim)])
    print(text, end="")
