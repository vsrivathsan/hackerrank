"""
https://www.hackerrank.com/challenges/angry-professor
"""


t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    on_time_cnt = 0
    for cur_st_time in a:
        if cur_st_time <= 0:
            on_time_cnt += 1
    if on_time_cnt >= k:
        print "NO"
    else:
        print "YES"
