#!/usr/bin/env python3Ω
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:35:03 2017
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
@author: jonbaird
"""
import numpy as np


def isprime(n):
    """
    determine if a number is a prime number
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif np.mod(n, 2) == 0 or np.mod(n, 3) == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if np.mod(n, i) == 0 or np.mod(n, i + 2) == 0:
            return False
        i += 6
    return True

primes = []
number = 1
while len(primes) < 10001:
    # for each number check if number is prime
    if isprime(number):
        primes.append(number)
    number += 1
print(primes[len(primes) - 1])
