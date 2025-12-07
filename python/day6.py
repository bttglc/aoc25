import sys
import operator
from functools import reduce

lines = sys.stdin.readlines()
symbols = lines[-1].strip().split()
sheet = [list(map(int, line.strip().split())) for line in lines[:-1]]

total = 0

for c in range(len(sheet[0])):
    operation = operator.add if symbols[c] == "+" else operator.mul
    total += reduce(operation, [item[c] for item in sheet])

print(total)
