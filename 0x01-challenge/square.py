#!/usr/bin/python3
"""
square
"""


class square():
    """class square"""

    width = 0

    def __init__(self, *args, **kwargs):
        """init"""

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """

        return self.width * self.width

    def PermiterOfMySquare(self):
        """permiter"""

        return (self.width * 4)

    def __str__(self):
        """str"""

        return "{}".format(self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
