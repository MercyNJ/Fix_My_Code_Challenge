#!/usr/bin/python3
""" A module that defines a class square."""

class Square():
    """ A square class."""
    
    def __init__(self, *args, **kwargs):
        """Initialization of a square instance"""
        self.width = 0
        self.height = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return str representation of square"""
        return "Square {}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
