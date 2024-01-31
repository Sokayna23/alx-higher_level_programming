#!/usr/bin/python3
"""find_peak function module"""


def find_peak(list_of_integers):
    """Determines the peak integer in a list"""
    peak = None
    for i in list_of_integers:
        if peak is None or i > peak:
            peak = i
        else:
            break
    return peak
