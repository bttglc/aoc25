import sys

total = 0

for line in sys.stdin.readlines():
    line = line.strip()
    digits = [int(x) for x in line]

    num_list = []
    start = 0
    length = len(digits)

    for i in range(11, -1, -1):
        max_value = max(digits[start : length - i])
        start += digits[start : length - i].index(max_value) + 1
        num_list.append(max_value)

    output = int("".join(str(num) for num in num_list))
    total += output

print(total)
