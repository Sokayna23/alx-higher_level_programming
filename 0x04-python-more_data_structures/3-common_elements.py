#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elmt = set()
    for item in set_1:
        if item in set_2:
            common_elmt.add(item)
    return (common_elmt)
