#!/usr/bin/python3
# 3-print_reserved_list_integer

def print_reversed_list_integer(my_list=[]):
    """print a list in reverse"""
    for elem in range(len(my_list)):
        my_list.reverse()
        return (my_list)