"""
Given a time in AM/PM format, convert it to military (2424-hour) time.

Note: Midnight is 12:00:0012:00:00 AM on a 1212-hour clock and 00:00:0000:00:00 on a 2424-hour clock. Noon is 12:00:0012:00:00 PM on a 1212-hour clock and 12:00:0012:00:00 on a 2424-hour clock.

Input Format

A time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01≤hh≤1201≤hh≤12.

Sample Input

Convert and print the given time in 2424-hour format, where 00≤hh≤2300≤hh≤23.

Sample Output

07:05:45PM
Explanation

19:05:45
"""

import sys


time = raw_input().strip()

hour_12_str = time.split(":")[0]
hour_12_int = int(hour_12_str)
if time.endswith("PM"):
    if hour_12_int == 12:
        hour_24 = hour_12_int
    else:
        hour_24 = hour_12_int + 12
    time = time.replace(hour_12_str, str(hour_24))
else:
    if hour_12_int == 12:
        hour_24 = "00"
        time = time.replace(hour_12_str, hour_24)


time = time[:-2]

print time
