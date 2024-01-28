#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in ops:
        a = int(argv[1])
        b = int(argv[3])
        print('{:d} {:s} {:d} = {:d}'.format(
            a, argv[2], b, ops[argv[2]](a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
