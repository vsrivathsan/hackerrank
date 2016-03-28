#!/bin/python

"""
You are given an array of integers of size NN. Can you find the sum of the elements in the array?

Input
The first line of input consists of an integer NN. The next line contains NN space-separated integers representing the array elements.
Sample:

66
11 22 33 44 1010 1111
Output
Output a single value equal to the sum of the elements in the array.
For the sample above you would just print 3131 since 1+2+3+4+10+11=311+2+3+4+10+11=31.
"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sum = 0
for item in arr:
    sum += item
print sum
