import sys

data = sys.stdin.read()
ranges, garbage = data.strip().split("\n\n")

ranges = ranges.splitlines()
ranges = [tuple(map(int, r.split("-"))) for r in ranges]

sum = 0
curr = 0

for s, e in sorted(ranges):
    sum = sum + max(curr, e + 1) - max(curr, s)
    curr = max(curr, e + 1)

print(sum)
