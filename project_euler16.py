"""
problem 16

pretty easy and quick with python

"""

n = str(2**1000)

s = 0

for i in range(len(n)):
    s += int(n[i])

print("ans:", s)
