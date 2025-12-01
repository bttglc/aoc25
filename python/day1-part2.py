import sys

D = 100

text = sys.stdin

i = 50
count = 0

for line in text:
    line = line.strip()

    direction = -1 if line[0] == "L" else 1

    shift = int(line[1:])

    complete_turns = shift // D
    shift = shift % D

    if shift > 0:
        new_i = i + direction * shift
        if (direction == 1 and new_i >= D) or (
            direction == -1 and new_i < 1 and i != 0
        ):
            count += 1
        i = new_i % D

    count += complete_turns

print("[Day 1, Part 2] Solution =", count)
