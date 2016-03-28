"""
Watson gives two integers (AA and BB) to Sherlock and asks if he can count the number of square integers between AA and BB (both inclusive).

Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.

Input Format
The first line contains TT, the number of test cases. TT test cases follow, each in a new line.
Each test case contains two space-separated integers denoting AA and BB.

Output Format
For each test case, print the required answer in a new line.

Constraints
1≤T≤1001≤T≤100
1≤A≤B≤1091≤A≤B≤109

Sample Input

2
3 9
17 24
Sample output

2
0
Explanation
Test Case #00: In range [3,9][3,9], 44 and 99 are the two square numbers.
Test Case #01: In range [17,24][17,24], there are no square numbers.
"""

def chk_if_pft_sqr(num):
    is_pft_sqr = False
    for cur_num in xrange(1, num+1):
        if cur_num*cur_num == num:
            is_pft_sqr = True
    return is_pft_sqr

def calc_sqr_ints(a, b):
    num_sqr_ints = 0
    for num in xrange(a, b+1):
        if chk_if_pft_sqr(num):
            num_sqr_ints += 1
    return num_sqr_ints

def main():
    t = int(raw_input().strip())
    for inp in xrange(t):
        inp_lst = raw_input().strip().split(" ")
        a = int(inp_lst[0])
        b = int(inp_lst[1])
        num_sqr_ints = calc_sqr_ints(a, b)
        print num_sqr_ints

main()
