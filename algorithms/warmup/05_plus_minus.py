"""
https://www.hackerrank.com/challenges/plus-minus
"""

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

pos_num = 0.0
neg_num = 0.0
zero_num = 0.0

for num in arr:
    if num > 0:
        pos_num += 1
    elif num < 0:
        neg_num += 1
    else:
        zero_num += 1

print pos_num/n
print neg_num/n
print zero_num/n
