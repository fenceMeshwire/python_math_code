#!/usr/bin/env python3

# Python 3.9.5

# factorial.py

def factorial(n):
    return n * factorial (n-1) if n > 1 else 1

if __name__ == '__main__':
    number:int = 7
    result = factorial(number)
    print(result)
