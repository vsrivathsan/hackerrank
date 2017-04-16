"""
https://www.hackerrank.com/challenges/utopian-tree
"""


def cal_height_after_n_cycles(n):
    height = 1
    if n == 1:
        return height*2
    for cycle in range(1, n+1):
        if cycle % 2 == 0:
            height = height+1
        else:
            height = height*2
    return height

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = cal_height_after_n_cycles(n=n)
    print height
