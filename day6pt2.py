#Advent of Code 2024
#12/6

import helpers as hp

map = hp.readIn()

# hp.pprint(map)

#if there is something in front of you turn right 90 degrees
#otherwise step forward.

pos = []
global dir
steps =[] # This will be a list of the steps including y, x, and dir

#Starting again for part 2

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "^":
            dir = 0
            pos = [i, j]
        elif map[i][j] == ">":
            dir = 1
            pos = [i, j]
        elif  map[i][j] == "<":
            dir = 3
            pos = [i, j]
        elif map[i][j] == "v":
            dir = 2
            pos = [i, j]
print(pos)
print(dir)

starty = pos[0]
startx = pos[1]


steps.append([pos[0], pos[1] ,dir])
print(steps)

def turnright():
    global dir
    # print(dir)
    if dir < 3:
        dir += 1
    else:
        dir = 0

def checkfront():
    global dir
    try:
        if dir == 0 and map[pos[0]-1][pos[1]] == '#':
            turnright()
            return True
        elif dir == 1 and map[pos[0]][pos[1]+1] == '#':
            turnright()
            return True
        elif dir == 2 and map[pos[0]+1][pos[1]] == '#':
            turnright()
            return True
        elif dir == 3 and map[pos[0]][pos[1]-1] == '#':
            turnright()
            return True
    except:
        return False
    return True

def step():
    global dir
    if dir == 0:
        pos[0] -= 1
    elif dir == 1:
        pos[1] += 1
    elif dir == 2:
        pos[0] += 1
    elif dir == 3:
        pos[1] -= 1    

loopcount = 0

def checkmap():
    global steps
    global loopcount
    while checkfront():
        step()
        newpos = [pos[0], pos[1], dir]
        if newpos in steps:
            # print(steps)
            loopcount += 1
            print("loop")
            steps = []
            return True
        steps.append(newpos)
    # print(steps)
    steps = []    
    return False

maxcount = len(map) * len(map[0])
current = 0

for y in range(len(map)):
    for x in range(len(map[y])):
        current += 1
        tempmap = hp.copylist(map)
        map[y] = map[y][:x] + '#' + map[y][x+1:]
        # hp.pprint(map)
        print(int(current/maxcount*100))
        pos = [starty, startx]
        dir = 0
        checkmap()
        map = hp.copylist(tempmap)

print(loopcount)

