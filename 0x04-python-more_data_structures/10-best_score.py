#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    bigest_int = None
    bigest_int_key = None
    for key, value in a_dictionary.items():
        if bigest_int is None or value > bigest_int:
            bigest_int_key = key
            bigest_int = value
    return (bigest_int_key)
