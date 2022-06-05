#!/usr/bin/env python3
# 5-no_c.py


def no_c(my_string):
    """remove all the c and C characters in a string"""

    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
