"""
https://www.hackerrank.com/challenges/a-very-big-sum
"""

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

sum = 0
for item in arr:
    sum += item

print sum
