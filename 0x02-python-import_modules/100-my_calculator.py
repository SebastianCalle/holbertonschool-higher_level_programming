#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    if (len(argv) != 4):
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    if (op != '+' and op != '-' and op != '*' and op != '/'):
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    if (argv[2] == '+'):
        result = add(int(argv[1]), int(argv[3]))
    if (argv[2] == '-'):
        result = sub(int(argv[1]), int(argv[3]))
    if (argv[2] == '/'):
        result = div(int(argv[1]), int(argv[3]))
    if (argv[2] == '*'):
        result = mul(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(argv[1], argv[2],
                                 argv[3], result))
