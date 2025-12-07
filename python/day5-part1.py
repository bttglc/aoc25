import sys

data = sys.stdin.read()
ranges, ingredients = data.strip().split("\n\n")

ranges = ranges.splitlines()
ranges = [tuple(map(int, r.split("-"))) for r in ranges]
ingredients = map(int, ingredients.splitlines())

fresh_count = 0

for i in ingredients:
    for el in ranges:
        if i >= el[0] and i <= el[1]:
            fresh_count += 1
            break

print(fresh_count)
