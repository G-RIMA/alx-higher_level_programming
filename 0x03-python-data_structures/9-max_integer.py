#!/usr/bin/python3
# 9-max_integer

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_no = my_list[0]
    for i in range(len(my_list)):
        if i > max_no:
            max_no = my_list[i]
            
    return max_no
