#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = argv[1]
    b = argv[3]
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] == "+":
        print(argv[1], '+', argv[3], '=', add(int(a), int(b)))
    elif argv[2] == "-":
        print(argv[1], '-', argv[3], '=', sub(int(a), int(b)))
    elif argv[2] == "*":
        print(argv[1], '*', argv[3], '=', mul(int(a), int(b)))
    elif argv[2] == "/":
        print(argv[1], '/', argv[3], '=', div(int(a), int(b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
