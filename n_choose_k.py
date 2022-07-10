#!/usr/bin/env python3

# Python 3.9.5

# n_choose_k.py

def n_choose_k(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
    
def factorial(n):
    return n * factorial (n-1) if n > 1 else 1
  
# Example:
if __name__ == '__main__':
    k = 2
    n = 5 
    result = n_choose_k(n, k)
    print(result)
    
