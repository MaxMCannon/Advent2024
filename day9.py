#Advent of Code 2024
#12/9
import helpers as hp

line = open('input.txt').read().splitlines()[0]

# print(line)

diskmap = []

file = True
currID = 0

for c in line:
    if file:
        for i in range(int(c)):
            diskmap.append(currID)
        currID += 1
        file = False
    else:
        for i in range(int(c)):
            diskmap.append('.')
        file = True

# print(diskmap)
dm2 = hp.copylist(diskmap)

for i in range(len(diskmap)):
    try:
        if diskmap[i] == '.':
            while diskmap[-1] == '.':
                diskmap.pop()
            diskmap[i] = diskmap[-1]
            diskmap.pop()
        # print(diskmap)
    except:
        print("done")
        break

checksum = 0
for i in range(len(diskmap)):
    checksum += i * diskmap[i]

print(checksum)

print(dm2)

openspaces = []
currID = dm2[-1]

def getspace(i):
    count = 0
    while dm2[i] == '.':
        count += 1
        i += 1
    print(count)
    return count

it = 0
while it < len(dm2):
    if dm2[it] == '.':
        