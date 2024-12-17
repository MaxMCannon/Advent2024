#day 10

import helpers as hp

map = hp.readIn()
nummap = []
for m in map:
    row = []
    for c in m: 
        row.append(int(c))
    print(row)
    nummap.append(row)

trailheads = []

for y in range(len(nummap)):
    for x in range(len(nummap[y])):
        if nummap[y][x] == 0:
            trailheads.append([y, x])

print(trailheads)

def createtrails(th):
    current = th
    curry = current[0]
    currx = current[1]
    trail = []
    try:
        if curry - 1 == nummap[curry][currx] + 1: #look up
            trail.append([curry-1][currx])
        if currx + 1 == nummap[curry][currx] + 1: #look right
            trail.append([curry][currx + 1])
        if curry + 1 == nummap[curry][currx] + 1: #look down
            trail.append([curry+1][currx])
        if currx - 1 == nummap[curry][currx] + 1: #look left
            trail.append([curry][currx-1])   
        print(trail)
    except:
        pass

for t in trailheads: 
    createtrails(t)
