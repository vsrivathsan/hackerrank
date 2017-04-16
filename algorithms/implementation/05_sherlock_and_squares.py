"""
https://www.hackerrank.com/challenges/sherlock-and-squares
"""


def calc_prfct_sqrs(a, b):
    sqrt_of_a = float(a**(0.5))
    sqrt_of_b = int(b**(0.5))
    if sqrt_of_a.is_integer():
        num_of_pft_sqrs = sqrt_of_b - int(sqrt_of_a) + 1
    else:
        num_of_pft_sqrs = sqrt_of_b - int(sqrt_of_a)
    return num_of_pft_sqrs


def main():
    t = int(raw_input().strip())
    for inp in xrange(t):
        inp_lst = raw_input().strip().split(" ")
        a = int(inp_lst[0])
        b = int(inp_lst[1])
        num_of_pft_sqrs = calc_prfct_sqrs(a, b)
        print num_of_pft_sqrs

main()
