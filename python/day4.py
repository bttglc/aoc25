import sys

from collections import defaultdict, Counter

input = sys.stdin.read()
matrix = [list(row) for row in input.splitlines()]
rows = len(matrix)
columns = len(matrix[0])

p1 = 0
p2 = 0
first = True

while True:
    changed = False
    for r in range(rows):
        for c in range(columns):
            neighbours = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < columns and matrix[rr][cc] == "@":
                        neighbours += 1
            if matrix[r][c] == "@" and neighbours < 5:
                p1 += 1
                changed = True
                if not first:
                    p2 += 1
                    matrix[r][c] = "."
    if first:
        print(p1)
        first = False
    if not changed:
        break

print(p2)
