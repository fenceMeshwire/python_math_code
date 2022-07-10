#!/usr/bin/env python3

# Python 3.9.5

# n_multichoose_k.py

def factorial(n):
    return n * factorial (n-1) if n > 1 else 1

def n_multichoose_k(n, k):
    return int(factorial(n + k - 1) / (factorial(n - 1) * factorial(k)))


if __name__ == '__main__':
    n = 5
    k = 3
    result = n_multichoose_k(n, k)
    print(result)
