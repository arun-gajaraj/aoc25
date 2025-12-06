import sys

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

lines = content.split("\n",-1)

fresh_ranges = []
stock_ids = []

for line in lines:
    if line.__contains__("-"):
        fresh_ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
    elif line == "":
        pass
    else:
        stock_ids.append(int(line))

pairs = sorted(fresh_ranges, key=lambda x: x[0])

fresh_count = 0
master_range = ()

for p in pairs:
    if master_range == ():
        master_range = p
        continue

    m = master_range

    if m[0] <= p[0] <= m[1] and p[1] > m[1]:
        master_range = (m[0], p[1])
    elif m[1] < p[0]:
        fresh_count += (m[1]+1 - m[0])
        master_range = p

fresh_count += (master_range[1]+1-master_range[0])
print(fresh_count)