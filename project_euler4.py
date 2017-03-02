#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:10:53 2017

@author: jonbaird

Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""
import math
P = 0
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        if (str(i*j) == str(i*j)[::-1]) and (i*j > P):
            P = i*j
print(P)

