#day 10

import helpers as hp

map = hp.readIn()
nummap = []
for m in map:
    row = []
    for c in m: 
        try:    
            row.append(int(c))
        except:
            pass
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
    step = 0
    trail = []
    while step <= 9:
        
        if curry > 0 and nummap[curry-1][currx] == step + 1: #look up
            trail.append([curry-1, currx])
            step += 1
            curry -= 1
        if currx < len(nummap[0])-1 and  nummap[curry-1][currx + 1] == step + 1: #look right
            trail.append([curry, currx + 1])
            step += 1
            currx  += 1 
        if curry < len(nummap)-1 and nummap[curry + 1][currx] == step + 1: #look down
            trail.append([curry+1, currx])
            step += 1
            curry += 1
        if currx > 0 and nummap[curry][currx - 1] == step + 1: #look left
            trail.append([curry, currx-1])   
            step += 1
            currx -= 1
        print(trail)

    print(trail)

for t in trailheads: 
    createtrails(t)
