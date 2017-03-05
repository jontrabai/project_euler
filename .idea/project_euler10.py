""" project euler problem #10 """

import numpy as np
from tqdm import tqdm_gui


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
for number in tqdm_gui(range(2000001)):
    # for each number check if number is prime
    if isprime(number):
        primes.append(number)
    number += 1
print(np.array(primes).sum())
