""" Doc String """
from __future__ import print_function
from __future__ import division
from pandas import DataFrame
from math import sqrt
from math import floor

triples = [[20, 99, 101], [60, 91, 109], [15, 112, 113], [44, 117, 125], [88, 105, 137], [17, 144, 145],
           [24, 143, 145], [51, 140, 149], [85, 132, 157], [119, 120, 169], [52, 165, 173], [19, 180, 181],
           [57, 176, 185], [104, 153, 185], [95, 168, 193], [28, 195, 197], [84, 187, 205], [133, 156, 205],
           [21, 220, 221], [140, 171, 221], [60, 221, 229], [105, 208, 233], [120, 209, 241], [32, 255, 257],
           [23, 264, 265], [96, 247, 265], [69, 260, 269], [115, 252, 277], [160, 231, 281], [161, 240, 289],
           [68, 285, 293]]

start = 1
stop = 1001

trips = []
for n in range(start, stop):
    for m in range(n + 1, stop):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if (a ** 2 + b ** 2 == c ** 2) and (a < b):
            if b < c:
                if sqrt(n ** 2 + m ** 2) % floor(sqrt(n ** 2 + m ** 2)) == 0:
                    trips.append([n, m, int(sqrt(n ** 2 + m ** 2))])
trips.sort()
df = DataFrame(trips, columns=['a', 'b', 'c'])
df['a_sqr'] = df['a'] ** 2
df['b_sqr'] = df['b'] ** 2
df['c_sqr'] = df['c'] ** 2
df['sum_abc'] = df['a'] + df['b'] + df['c']
print(df.head())

my_sum = 1000
for a in range(1, int(my_sum / 3)):
    for b in range(a + 1, int(my_sum / 2)):
        c = my_sum - a - b
        if (a * a + b * b) == c * c:
            print(a, b, c)
