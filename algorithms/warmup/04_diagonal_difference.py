"""
https://www.hackerrank.com/challenges/diagonal-difference
"""

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)

pri_diag_sum = 0
sec_diag_sum = 0

for row_idx in xrange(len(a)):
    row = a[row_idx]
    for col_idx in xrange(len(row)):
        elem = row[col_idx]
        if row_idx == col_idx:
            pri_diag_sum += elem
    for col_idx in xrange(len(row)):
        elem = row[col_idx]
        if col_idx == n-row_idx-1:
            sec_diag_sum += elem

print abs(pri_diag_sum - sec_diag_sum)
