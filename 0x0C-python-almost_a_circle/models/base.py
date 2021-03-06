#!/usr/bin/python3
"""
class Base
"""
import json
import os.path
import csv
import turtle


class Base:
    """
    Class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialziate attributes
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Drae rectangles and squares"""
        wn = turtle.Screen()
        wn.bgcolor("black")
        tt = turtle.Turtle()
        tt.color("cyan")
        tt.shape("turtle")

        for rec in list_rectangles:
            print(rec)
            for i in range(2):
                tt.forward(rec.width)
                if rec.id % 2 == 0:
                    tt.right(90)
                else:
                    tt.left(90)
                tt.forward(rec.height)
                if rec.id % 2 == 0:
                    tt.right(90)
                else:
                    tt.left(90)
        tt.goto(-100, 0)
        for squ in list_squares:
            for i in range(4):
                print(squ)
                tt.forward(squ.size)
                if rec.id % 2 == 0:
                    tt.right(90)
                else:
                    tt.left(90)

        turtle.done()


    @staticmethod
    def from_json_string(json_string):
        """
        return a list from JSON string
        """
        list_obj = []
        if json_string is None or json_string == "":
            return list_obj
        else:
            list_obj = json.loads(json_string)
            return list_obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return a list to JSON string
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            new_i = cls(1, 1)
            new_i.update(**dictionary)
        if cls.__name__ == 'Square':
            new_i = cls(1)
            new_i.update(**dictionary)

        return new_i

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        """
        if list_objs:
            list_d = []
            for obj in list_objs:
                if isinstance(obj, cls):
                    with open(cls.__name__ + '.json', 'w') as f:
                        dict1 = obj.to_dictionary()
                        list_d.append(dict1)
                        data = cls.to_json_string(list_d)
                        f.write(data)
        else:
            with open(cls.__name__ + '.json', 'w') as f:
                data = cls.to_json_string(list_objs)
                f.write(data)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        li = []
        new_li = []
        if cls.__name__ == 'Rectangle':
            filename = 'Rectangle.json'
        if cls.__name__ == 'Square':
            filename = 'Square.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                data = f.read()
                li = cls.from_json_string(data)
                for i in range(len(li)):
                    new_li.append(cls.create(**li[i]))

                return new_li
        else:
            return li

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save in a csv file
        """
        if cls.__name__ == 'Rectangle':
            filename = 'Rectangle.csv'
            header = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            filename = 'Square.csv'
            header = ['id', 'size', 'x', 'y']
        if list_objs:
            with open(filename, 'w') as f:
                csv_w = csv.DictWriter(f, fieldnames=header)
                csv_w = csv.DictWriter(f, fieldnames=header)
                csv_w.writeheader()
                for obj in list_objs:
                    dict1 = obj.to_dictionary()
                    if isinstance(obj, cls):
                        csv_w.writerow(dict1)

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instances
        """
        li = []
        new_li = []
        if cls.__name__ == 'Rectangle':
            filename = 'Rectangle.csv'
        if cls.__name__ == 'Square':
            filename = 'Square.csv'
        if os.path.isfile(filename):
            dict2 = {}
            with open(filename, 'r') as f:
                csv_r = csv.DictReader(f)
                for row in csv_r:
                    for key, value in row.items():
                        dict2[key] = int(value)
                    new_li.append(cls.create(**dict2))
                return new_li
        else:
            return li
