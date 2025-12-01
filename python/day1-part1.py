import sys

D = 100
i = 50
count = 0

for line in sys.stdin:
    direction = -1 if line[0] == "L" else 1

    i = (i + direction * int(line[1:])) % D

    if i == 0:
        count += 1

print("[Day 1, Part 1] Solution =", count)
