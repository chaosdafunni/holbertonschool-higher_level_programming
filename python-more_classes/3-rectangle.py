#!/usr/bin/python3
"""Define a class named Rectangle."""


class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiation with optionals.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Function to set the width of the rectangle.

        Args:
            value (int): must be an int.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function to retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function to set the height of the rectangle.

        Args:
            value (int): must be an int.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This function returns the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """This function returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__height + self.__width + self.__width)

    def __str__(self):
        """Function that prints the rectangle with the # characters

        Returns:
            str: # character * height * width
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            return "\n".join(["#" * self.__width
                              for i in range(self.__height)])
