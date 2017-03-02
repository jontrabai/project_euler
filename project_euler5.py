#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:04:10 2017

@author: jonbaird

Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""

# %%
is_target = 0
number = 2520
divisors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while not is_target:
    total = 0
    remainders = [number % x for x in divisors]
    for i in remainders:
        if i > 0:
            is_target = 0
            number += 2520
            break
        else:
            is_target = 1
print(number)
