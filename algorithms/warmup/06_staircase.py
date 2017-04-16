"""
https://www.hackerrank.com/challenges/staircase
"""

n = int(raw_input().strip())
op = ''

for i in range(0, n):
    for j in range(0, (n-1)-i):
        op += ' '
    for x in range((n-1)-i, n):
        op += '#'
    op += '\n'

print op
