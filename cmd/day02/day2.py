import sys

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

ranges = content.split(",",-1)

invalid_sum = 0

rl = []

for r in ranges:
    x, y = map(int, r.split("-"))
    rl.append((x,y))

for i in range(1, 100000):
    val = int(str(i) * 2)

    for j, k in rl:
        if j <= val <= k:
            invalid_sum += val

print("Part 1: ", invalid_sum)

p2set = set()

for i in range(1, 100000):

    for p in range(2, 10):

        val = int(str(i) * p)

        for j, k in rl:
            if j <= val <= k:
                p2set.add(val)

print("Part 2: ", sum(p2set))