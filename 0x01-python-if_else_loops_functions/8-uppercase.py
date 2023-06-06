#!/usr/bin/python3

def uppercase(str):
    for c in range(0, len(str)):
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
