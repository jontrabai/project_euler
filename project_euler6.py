#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:03:52 2017

@author: jonbaird

Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""
import numpy as np
from tqdm import tqdm


def ssq(stop=10):
    """
    compute the sum of squares
    """
    total = 0
    squares = [i ** 2 for i in tqdm(range(1, stop + 1))]
    while len(squares) > 0:
        total += squares.pop()
    return total


def sqs(stop=10):
    """
    sequence is a 'range' variable
    compute the square of the sum of 'sequence'
    """
    total = 0
    for i in tqdm(np.arange(1, stop + 1)):
        total = total + i
    return total * total

print(ssq(stop=10000) - sqs(10000))
print(sqs(stop=10000) - ssq(stop=10000))
