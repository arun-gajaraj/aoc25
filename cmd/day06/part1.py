import sys

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

lines = content.split("\n",-1)
lc = len(lines)
wc = len(lines[0].split())

l1, l2, l3, l4, s1 = lines[0].split(), lines[1].split(), lines[2].split(), lines[3].split(), lines[4].split()
total_sum = 0

for i in range(wc):
    if s1[i] == "+":
        sum = int(l1[i]) + int(l2[i]) + int(l3[i]) + int(l4[i])
        total_sum += sum
    elif s1[i] == "*":
        product = int(l1[i]) * int(l2[i]) * int(l3[i]) * int(l4[i])
        total_sum += product

print(total_sum)
