"""
https://www.hackerrank.com/challenges/time-conversion
"""

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
