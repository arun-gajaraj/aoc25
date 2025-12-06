import sys
import math

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

lines = content.split("\n",-1)
lc = len(lines)

# character count is 3730
total_sum = 0
current_nums = []

for c in range(len(lines[0])-1, -1, -1):
    num_col = ""
    sym = ""
    add_curr = False

    for l in range(len(lines)):
        char = lines[l][c]
        if char==" ":
            pass
        elif char =="+" or char == "*":
            sym = char
            add_curr = True
            break
        else :
            num_col += char
    if num_col == "":
        continue
    current_nums.append(int(num_col))
    if add_curr:
        if sym == "+":
            total_sum += sum(current_nums)
        elif sym == "*":
            total_sum += math.prod(current_nums)
        sym = ""
        current_nums = []
print(total_sum)
