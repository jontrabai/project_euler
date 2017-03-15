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
    def factor(n=1):
        """ factor a number brute force """
        factors = []
        for number in range(1, n + 1):
            if n % number == 0:
                factors.append(number)
        return factors

    @staticmethod
    def factor_e(n=1):
        """ factor a number brute force + """
        factors = []
        for x in range(n + 1, int(np.ceil(np.sqrt(n))), -1):
            if n % x == 0:
                factors.append(int(n / x))
                factors.append(x)
        return factors

    @staticmethod
    def valid_ending(n=1):
        """ test if a number ends with a valid number for perfect square """
        num_len = len(str(n)) - 1
        if str(n)[num_len] == '2' or str(n)[num_len] == '3' or str(n)[num_len] == '7' or str(n)[num_len] == '8':
            return False
        elif str(n)[num_len] == '0':
            count = 1
            p = num_len - 1
            while str(n)[p] == '0':
                count += 1
                p -= 1
            if count % 2 == 0:
                return True
            else:
                return False
        else:
            return True

    @staticmethod
    def strip_trailing_zeros(n=1):
        """
        strip trailing zeroes from a number
        """
        return int(str(n).rstrip('0'))

    @staticmethod
    def fermat_factor(n=1):
        """
        FermatFactor(N): // N should be odd
        a ← ceil(sqrt(N))
        b2 ← a*a - N
        while b2 is not a square:
            a ← a + 1    // equivalently: b2 ← b2 + 2*a + 1
            b2 ← a*a - N //               a ← a + 1
        endwhile
        return a - sqrt(b2) // or a + sqrt(b2)
        """
        a = np.ceil(np.sqrt(n))
        b = a * a - n
        # TODO: add while loop
        return a - np.sqrt(b)

    @staticmethod
    def find_digital_root(n=1):
        """
        perfect squares have digital roots 1, 4, 7, or 9
        """
        num = str(n)
        number_list = []
        while len(num) > 2:
            numsum = 0
            for num_i in range(len(num)):
                number_list.append(num[num_i])
            for num_i in range(len(number_list)):
                numsum += int(number_list[num_i])
            num = str(numsum)
        while len(str(num)) == 2:
            numsum = int(str(num)[0]) + int(str(num)[1])
            num = int(numsum)
        return int(num)

    @staticmethod
    def examine_unit_digit(n=1):
        num = str(n)
        if len(num) > 1:
            unit_digit = int(num[len(num) - 1])
            tens_digit = int(num[len(num) - 2])
            print(tens_digit, unit_digit)
            if unit_digit == 5:
                if tens_digit == 2:
                    return True
            elif unit_digit == 6:
                if (tens_digit % 2) == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def is_divisible_by_4(n=1):
        if n % 4 == 0:
            if (n * n) / 8 == 0:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    e = Euler12()
    m = e.tri(7)
    l = e.factor_e(m)
    # not the point of the question but interesting ...
    # print(l)
    i = 1
    while len(e.factor_e(e.tri(i))) < 50:
        i += 1
    f = e.factor(e.tri(i))
    print(len(e.factor_e((e.tri(i)))))
