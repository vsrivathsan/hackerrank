"""
https://www.hackerrank.com/challenges/cut-the-sticks
"""

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
while True:
    op_arr = list()
    cur_min = min(arr)
    print len(arr)
    for el in arr:
        if el - cur_min > 0:
            op_arr.append(el-cur_min)
    len_op_arr = len(op_arr)
    if len_op_arr > 0:
        arr = op_arr
        continue
    else:
        break
