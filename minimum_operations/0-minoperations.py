#!/usr/bin/python3

"""
Given a number n, write a method that calculates the fewest # of operations.

Creating the prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    if n <= 1:
        return 0
    factors = []
    f = 2
    while f * f <= n:
        while (n % f) == 0:
            factors.append(f)
            n //= f
        f += 1
    if n > 1:
        factors.append(n)
    # Calculating the minimun operations using the prime factors
    min_operations = sum(factors)
    return min_operations
