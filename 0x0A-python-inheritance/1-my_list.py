#!/usr/bin/python3
"""
    function that print sorted list
"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """print list sorted"""
        print(sorted(self))
