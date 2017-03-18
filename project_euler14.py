"""
project euler problem # 14
"""


def make_seq(n=0):
    seq = [n]
    count = 0
    while seq[count] > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        seq.append(int(n))
        count += 1
    return seq


largest = 0
collatz_start = 0
for i in range(13):
    seq_length = len(make_seq(i))
    if seq_length >= largest:
        largest = seq_length
        collatz_start = i
print(largest, collatz_start)
