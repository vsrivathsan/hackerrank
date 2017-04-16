"""
https://www.hackerrank.com/challenges/sherlock-and-the-beast
"""


def construct_large_dec_num(n, dec_num):
    """Construct large decimal number."""
    cur_dec_num = ""
    while len(cur_dec_num) < n:
        cur_dec_num += "3" * 5
        if (n - len(cur_dec_num)) % 3 == 0:
            cur_dec_num = "5" * 3 * ((n - len(cur_dec_num)) / 3) + cur_dec_num
    if len(cur_dec_num) <= n:
        dec_num = update_dec_num(dec_num=dec_num, cur_dec_num=cur_dec_num)
    return dec_num


def update_dec_num(dec_num, cur_dec_num):
    if dec_num != "":
        if int(dec_num) < int(cur_dec_num):
            dec_num = cur_dec_num
    else:
        dec_num = cur_dec_num
    return dec_num

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    num_list = list()
    dec_num = ""
    if n < 3:
        dec_num = "-1"
    else:
        if n % 3 == 0:
            dec_num = "5" * n
        else:
            if n % 5 == 0:
                cur_dec_num = "3" * n
                dec_num = update_dec_num(dec_num=dec_num, cur_dec_num=cur_dec_num)

            dec_num = construct_large_dec_num(n=n, dec_num=dec_num)

    if len(dec_num) != n:
        dec_num = "-1"

    if dec_num != "":
        # print "n: {0}, dec_num: {1}".format(n, dec_num)
        print dec_num
