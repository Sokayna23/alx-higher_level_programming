#!/usr/bin/python3
"""find_peak function module"""

def find_peak(list_of_integers):
	n = len(list_of_integers);
	for i in range(n):
		if (i == 0 or list_of_integers[i] >= list_of_integers[i - 1]) and (i == n - 1 or list_of_integers[i] >= list_of_integers[i + 1]):
			return (list_of_integers[i])
	return (None)
