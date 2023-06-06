#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):
        if abs(number) % 3 == 0:
            print("Fizz", end=" ")
        elif abs(number) % 5 == 0:
            print("Buzz", end=" ")
        elif abs(number) % 3 == 0 and abs(number) % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(number), end=" ")
