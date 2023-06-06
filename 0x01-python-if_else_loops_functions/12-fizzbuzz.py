#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):
        fizz = abs(number) % 3
        buzz = abs(number) % 5
        if fizz == 0:
            print("Fizz", end=" ")
        elif buzz == 0:
            print("Buzz", end=" ")
        elif fizz == 0 and buzz == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(number), end=" ")
