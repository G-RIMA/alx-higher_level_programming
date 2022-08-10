#!/usr/bin/python3
# 1-rectangle.py

<<<<<<< HEAD
"""Defines a rectangle class"""


class Rectangle:
    """REpresents a rectangle"""

    def __init__(self, width=0, height=0):
        """inisialize the rectangle
        Inputs:
           width (int): The width of the rectangle
           height (int): The height of the rectangle
          

=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
>>>>>>> baed3b5763e6cd2c19c09f7981157420fcc13b6f
        """
        self.width = width
        self.height = height

<<<<<<< HEAD
    """property"""
    def width(self):
        """Get width"""
        return self.__width

    """width.setter"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
=======
    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
>>>>>>> baed3b5763e6cd2c19c09f7981157420fcc13b6f
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

<<<<<<< HEAD
    #property
    def height(self):
        """get the height of rectangle"""
        return self.__height

    #height_setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError(" height must be >= 0")
        self.__height = value
    
=======
    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
>>>>>>> baed3b5763e6cd2c19c09f7981157420fcc13b6f
