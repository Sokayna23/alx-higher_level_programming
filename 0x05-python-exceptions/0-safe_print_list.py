#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elements++
    except IndexError:
        break
    print("")
    return (elements)
