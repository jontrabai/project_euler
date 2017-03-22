"""
problem 17
"""


def num_letters(digit=0, place=0):
    """
    count the number of letters in a digit
    :param digit: a digit from 0 to 9
    :return: number of letters in the english word for n
    """
    ones = {0: 4, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
    if place == 0:
        return ones[digit]
    elif place == 2:
        return ones[digit] + 7
    elif place == 3:
        return ones[digit] + 12


total = 0
for num in range(1000, 1001):
    idx = 0
    for n in str(num)[::-1]:
        print(num, num_letters(int(n)))
        total += num_letters(int(n), place=2)
    print(total)
print(total)
