#Advent of Code 2024
#12/9

line = open('input.txt').read().splitlines()[0]

# print(line)

diskmap = ''

file = True
currID = 0

for c in line:
    if file:
        diskmap += str(currID) * int(c)
        currID += 1
        file = False
    else:
        diskmap += '.' * int(c)
        file = True

print(diskmap)
countnums = 0

for c in line:
    if c.isnumeric():
        countnums += 1

def getlast():
    global diskmap
    last = len(diskmap)-1
    while not diskmap[last].isnumeric():
        last -= 1
    out = diskmap[last]
    # print(diskmap[last])
    diskmap = diskmap[:last]
    return out


checksum = 0
for i in range(len(diskmap)):
    if diskmap[i] == '.':
        checksum += i * int(getlast())
    else:
        checksum += i * int(diskmap[i])
    print(checksum)


# def getlast():
#     global diskmap
#     out = ''
#     for i in range(len(diskmap)-1, 0, -1):
#         if diskmap[i] != '.':
#             out = diskmap[i]
#             # print(out)
#             diskmap = diskmap[:i] + '.' + diskmap[i+1:]
#             break
#     return out

# for i in range(countnums):
#     if diskmap[i] == '.':
#         diskmap = diskmap[:i] + getlast() + diskmap[i+1:]
#         # print(diskmap)

# checksum = 0
# for i in range(countnums):
#     checksum += i * int(diskmap[i])

# print(checksum)

        
