"""
projecte euler 15
I had to look up the answer to this one
http://joaoff.com/2008/01/20/a-square-grid-path-problem/
i knew it had something to do with factorials
"""
from math import factorial

grid_size = 20
# the binomial coefficient equation
# (2n)! / (n!n!)
print("ans:", int(factorial(2 * grid_size) / (factorial(grid_size) *
                                              factorial(grid_size))))
