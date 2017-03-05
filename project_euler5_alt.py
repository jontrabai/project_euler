#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:52:35 2017

@author: jonbaird
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

"""

# Algorithm ===================================================================
#  k = 20
#  N = 1
#  i = 1
#  check = true
#  limit = sqrt(k)
#  while p[i] <= k
#      a[i] = 1
#      if check then
#          if p[i] <= limit then
#              a[i] = floor( log(k) / log(p[i]) )
#          else
#              check = false
#          end if
#      end if
#  N = N * p[i] ^ a[i]
#  i = i + 1
#  end while
#  output N
# ============================================================================

import math
import numpy as np


def prime_gen(size_limit):
    """
    generate prime number sequence up to n
    using the sieve of Eratosthenes
    """
    nums = list(np.arange(2, size_limit + 1))
    composites = []
    index = 0
    while index < len(nums):
        for iterator in range(len(nums)):
            if nums[index] * nums[iterator] in nums:
                composites.append(nums[index] * nums[iterator])
        index += 1
    return list(set(nums) - set(composites))

k = 200
N = 1
i = 1
check = True
limit = math.sqrt(k)
a = []
# for prime in prime_gen(k):
#     a.append(1)
#     if check:
#         if prime <= limit:
#             a.pop()
#             a.append(math.floor(math.log(k)/math.log(prime)))
#         else:
#             check = False
#     N = N * prime**a[i-1]
#     i += 1
numbers = prime_gen(1001)  # print the result to the console
numbers.sort()
print(numbers[len(numbers) - 1])
