#!/usr/bin/python3

for c in range(ord('Z'), ord('A') -1, -1):
    char = chr(c)
    print(char, end='')
    if c % 2 == 0:
        print(char.upper(), end="")
print()
