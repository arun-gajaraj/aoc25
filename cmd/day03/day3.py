import sys

fileName = sys.argv[1]
print("reading file: ", fileName)

with open(fileName, 'r') as file:
    content = file.read()

lines = content.split("\n",-1)

largest_sum = 0

for line in lines:
    l = len(line)
    large = 0
    for i in range(0, l-1):
        for j in range (1, l):
            if i >= j :
                continue
            temp = int(line[i]+line[j])
            if large < temp:
                large = temp
    largest_sum += large


print("Part 1 : ", largest_sum)

p2sum = 0
pack_length = 12

fetched_nums = ""

for line in lines:
    line_sum = 0
    
    fetched_nums = ""

    def do(start_idx: int, fetched: int) :
        global p2sum
        global fetched_nums 
        largest_idx = -1
        temp_n = -1
        if start_idx >= len(line) or len(fetched_nums) == pack_length:
            return
        for  idx in range(start_idx, len(line)):
            # print(f"processing {line[idx]}")


            if len(line)- (idx+1) < pack_length - len(fetched_nums)-1:
                break

            if int(line[idx]) > temp_n:
                temp_n = int(line[idx])
                largest_idx = idx

        # print(f"largest idx : {largest_idx}, value: {temp_n}")
        # print("temp_n", temp_n)
        fetched_nums += str(temp_n)
        do(largest_idx+1, 0) 
    do(0, 0)
    print("pack: ", fetched_nums)
    p2sum += int(fetched_nums)

print(f"p2sum: {p2sum}")
