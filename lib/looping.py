#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squared_list = [num ** 2 for num in int_list]
    return squared_list
    pass

def fizzbuzz():
    for num in range(1, 101):
        print(fizzbuzz_printer(num))
    pass

def fizzbuzz_printer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
    