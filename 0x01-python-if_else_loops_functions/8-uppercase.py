#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) > 96 and ord(letter) < 123):
            letter2 = ord(letter) - 32
            print('{:c}'.format(letter2), end='')
        else:
            print('{}'.format(letter), end='')
    print('')
