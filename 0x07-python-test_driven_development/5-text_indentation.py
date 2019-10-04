#!/usr/bin/python3
"""
    function that prints a text whit
    2 new lines after each of these
    characters . ? :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = ".?:"
    i = 0
    flag = 0
    while i < len(text):
        if text[i] == " " and i == 0:
            while text[i] == " ":
                i += 1
        if i < len(text) - 1:
            for j in range(len(characters)):
                if text[i] == characters[j]:
                    print("{}".format(text[i]))
                    flag = 1
                    i += 1
            if text[i] == " " and flag == 1:
                print("")
                while text[i] == " ":
                    i += 1
                flag = 0

        print("{}".format(text[i]), end="")
        i += 1
