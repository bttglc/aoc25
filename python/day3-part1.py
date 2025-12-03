import sys

total = 0

for line in sys.stdin.readlines():
    line = line.strip()
    digits = [int(x) for x in line]

    deca = max(digits[:-1])
    idx = digits.index(deca)
    deci = max(digits[idx + 1 :])

    total += 10 * deca + deci

print(total)
