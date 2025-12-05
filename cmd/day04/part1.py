import sys

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

lines = content.split("\n",-1)

rows = len(lines)
cols = len(lines[0])

# Convert each string to a list of characters
matrix = [list(line) for line in lines]

# x,y
dirs = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
forkable = []

for y in range(len(lines)):
    for x in range(len(lines[y])):

        adjCount = 0

        if lines[y][x] != "@":
                continue

        for dx,dy in dirs:

            if x+dx < 0 or x+dx >= len(lines[y]) or y+dy < 0 or y+dy >= len(lines):
                continue
            
            if lines[y+dy][x+dx] == "@":
                adjCount += 1
            elif lines[y+dy][x+dx] == ".":
                pass
        if adjCount < 4:
            forkable.append((x,y))
            matrix[y][x] = "x" 

print(forkable)
print(len(forkable))


