#!/usr/bin/python3
# 3-print_reserved_list_integer


def print_reversed_list_integer(my_list=[]):
    """print a list in reverse"""
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
