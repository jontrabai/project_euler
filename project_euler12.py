""" Problem #12"""


class Euler12(object):

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
