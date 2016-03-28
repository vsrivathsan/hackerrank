"""
Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. Print the decimal value of each fraction.

Input Format

The first line, NN, is the size of the array.
The second line contains NN space-separated integers describing the array of numbers (A1,A2,A3,⋯,ANA1,A2,A3,⋯,AN).

Output Format

Print each value on its own line with the fraction of positive numbers first, negative numbers second, and zeroes third.

Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The fraction of the positive numbers, negative numbers and zeroes are 36=0.50000036=0.500000, 26=0.33333326=0.333333 and 16=0.16666716=0.166667, respectively.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10−410−4 are acceptable.
"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

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
