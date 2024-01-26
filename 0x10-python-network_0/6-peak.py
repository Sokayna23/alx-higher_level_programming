#!/usr/bin/python3
"""find_peak function module"""

def find_peak(list_of_integers):
	if not list_of_integers:
		return (None)
	n = len(list_of_integers);
	left, right = 0, n - 1
	while left < right:
		mid = (left + right) // 2
		if (list_of_integers[mid] > list_of_integers[mid + 1]):
			right = mid
		else:
			left = mid + 1
	return list_of_integers[right] if right > 0 else list_of_integers[0]

