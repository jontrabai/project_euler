"""
problem 92
"""


def sum_sqr_dig(n=1):
    """
    Add the squares of the digits of a number
    :param n: an integer
    :return: the sum of the sqares of the digits of n
    """
    nstr = str(n)
    nl = []
    result = 0
    for itx in range(int(len(nstr))):
        nl.append(int(nstr[itx]) ** 2)
    for itx in range(len(nl)):
        result += nl[itx]
    return result


def make_seq(n=1):
    """
    combine the squares of the digits of a number into a sequence
    :param n: the starting number
    :return: the sequence of numbers
    """
    l = [n]
    idx = 0
    while sum_sqr_dig(l[idx]) >= 1 or sum_sqr_dig(l[idx]) != 89:
        if sum_sqr_dig(l[idx]) == 1 or sum_sqr_dig(l[idx]) == 89:
            l.append(sum_sqr_dig(l[idx]))
            break
        else:
            l.append(sum_sqr_dig(l[idx]))
            idx += 1
    return l


num_end = 10000000
count_89 = 0
count_1 = 0
for i in range(1, num_end):
    seq = make_seq(i)
    if seq[len(seq) - 1] == 1:
        count_1 += 1
    elif seq[len(seq) - 1] == 89:
        count_89 += 1
    else:
        raise Exception

print("ends with 1:", count_1)
print("ends with 89:", count_89)
