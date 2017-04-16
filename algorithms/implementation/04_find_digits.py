"""
https://www.hackerrank.com/challenges/find-digits
"""


def cal_evenly_div_digits(n):
    num_evenly_div_digits = 0
    for digit_str in str(n):
        digit = int(digit_str)
        if digit == 0:
            continue
        if n % digit == 0:
            num_evenly_div_digits += 1
    return num_evenly_div_digits

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    num_even_div_digits = cal_evenly_div_digits(n=n)
    print num_even_div_digits
