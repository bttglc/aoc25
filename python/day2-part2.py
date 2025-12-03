import sys
import re

pattern = r"^(\d+)(\1)+$"
sum = 0


interval_list = sys.stdin.readline().split(",")
intervals = [tuple(map(int, item.split("-"))) for item in interval_list]

for interval in intervals:
    for i in range(interval[0], interval[1] + 1):
        if re.match(pattern, str(i)):
            sum += i

print(sum)
