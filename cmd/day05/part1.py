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

fresh_stock = []

for id in stock_ids:
    for left, right in fresh_ranges:
        if left <= id <= right:
            fresh_stock.append(id)
            break

print(len(fresh_stock))
