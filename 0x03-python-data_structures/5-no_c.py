#!/usr/bin/env python3
#5-no_c.py


def no_c(my_string):
    """remove all the c and C characters in a string"""
    x = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(x))
