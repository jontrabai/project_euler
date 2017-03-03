#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 08:36:30 2017

@author: jonbaird

Problem from Project Euler web site
find the sum of the factors of 3 or 5
that are less than 1000
"""

# ==========================================================================
# Function factors
# ============================================================================

def factors(xfactor=3, yfactor=5, limit=1000):
    """
    return a list containing the factors of xfactor OR yfactor
    """
    numbers = []
    for number in range(limit):
        if number % xfactor == 0 or number % yfactor == 0:
            numbers.append(number)

    return numbers





# %%==========================================================================
# Function sum_list
# ============================================================================


def sum_list(list1):
    """
    return the sum of a list of numbers
    """
    total = 0
    while len(list1) > 0:
        total = total + list1.pop()
    return total

# ==========================================================================
#  Main Program
# ============================================================================
FACTOR_LIST = factors(3, 5, 1000)
SUM_OF_FACTORS = sum_list(FACTOR_LIST)
print(SUM_OF_FACTORS)

