#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    r3 = Square(4)
    r4 = Square(9)
    Square.save_to_file(None)

    with open("Square.json", "r") as file:
        print(file.read())
