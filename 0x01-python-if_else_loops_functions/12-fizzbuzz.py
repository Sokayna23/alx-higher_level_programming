#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):
        fizz = abs(number) % 3
        buzz = abs(number) % 5
        fizzbuzz = abs(number) % 15
        
        if fizz == 0:
            print("Fizz", end=" ")
        if buzz == 0:
            print("BUZZ")
        if fizzbuzz == 0:
            print("FizzBuzz", end=" ")
        else:
            print(number, end=" ")
