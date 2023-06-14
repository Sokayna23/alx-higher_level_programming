#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (0)
    for pair in my_list:
        x = sum(map(lambda pair: pair[0] * pair[1], my_list))
        y = sum(map(lambda pair: pair[1], my_list))
        if y == 0:
            return (0)
        average = x / y
    return (average)
