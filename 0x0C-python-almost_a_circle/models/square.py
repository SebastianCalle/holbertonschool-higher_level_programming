#!/usr/bin/python3

from .rectangle import Rectangle
"""import models"""

class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """Return string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Return private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update class Square"""
        if args:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                elif key == 'size':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """Return dictionary of attributes"""
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Square__size']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
