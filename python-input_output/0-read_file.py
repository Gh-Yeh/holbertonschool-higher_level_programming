#!/usr/bin/python3
"""Defines a function to read a file and print it to stdout."""


def read_file(filename=""):
    """function that reads a text file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
