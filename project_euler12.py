""" Problem #12"""

import numpy as np


class Euler12(object):

    def __init__(self):
        pass

    def tri(self, n=1):
        """ calculate triangle number """
        try:
            assert(n >= 0)
        except AssertionError:
            print("please supply an number >= 0")
            return -1
        else:
            return self._tri(n)

    @staticmethod
    def _tri(n=1):
        """ return total """
        tot = 0
        for x in range(1, n + 1):
            tot += x
        return tot

    @staticmethod
    def factor(num=0):
        """
        factor a number
        :param num: natural number
        :return: set of factors
        """
        factors = [1]
        divisor = 2
        while divisor <= np.ceil(np.sqrt(num)):
            if num % divisor == 0:
                factors.append(divisor)
            divisor += 1
        for fac in set(factors):
            factors.append(int(num / fac))

        return set(factors)

if __name__ == '__main__':
    e = Euler12()
    m = e.tri(7)
    i = 1
    while len(e.factor(e.tri(i))) < 500:
        i += 1
    f = e.factor(e.tri(i))
    print("number of factors:", len(e.factor((e.tri(i)))))
    print("answer:", e.tri(i))
