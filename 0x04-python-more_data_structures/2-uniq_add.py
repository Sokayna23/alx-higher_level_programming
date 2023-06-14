#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    unique_nums = set(my_list)
    unique_sum = sum(map(lambda num: int(num), unique_nums))
    return (unique_sum)
