#!/usr/bin/python3
""" A module that defines a class square."""


class Square():
    """ A square class."""
    def __init__(self, width, height):
        """Initialization of a square instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width's attribue setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height attribute's getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attributes's setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return str representation of square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create an instance"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
