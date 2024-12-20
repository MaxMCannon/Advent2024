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

# print(dm2)

def getspaces():
    spaces = []
    count = 0
    for i in range(len(dm2)):
        if dm2[i] == '.':
            count += 1
        else:
            if count > 0:
                spaces.append([i-count, count])
                count = 0
    return spaces

map = []
def getlens():
    global map
    ID = 0
    count = 0
    i = 0
    while i < len(dm2)+1:
        if i >= len(dm2):
            map.append([ID, count])
            break
        if dm2[i] == ID:
            count += 1
            i += 1
        else:
            while dm2[i] == '.':
                i += 1
            map.append([ID, count])
            count = 0
            ID += 1

getlens()
map = hp.reverseList(map)
# print(map)
print(getspaces())
lastID = dm2[-1]

for m in map:
    for s in getspaces():
        if m[1] <= s[1]:
            if m[0] in dm2[:s[0]]:
                break
            while m[0] in dm2:
                for i in range(len(dm2)):
                    if dm2[i] == m[0]:
                        dm2[i] = '.'
            for i in range(s[0], s[0] + m[1]):
                dm2[i] = m[0]
            # print(dm2)
            break

checksum2 = 0
for i in range(len(dm2)):
    if dm2[i] != '.':
        checksum2 += i * dm2[i]

print(checksum2)