#Advent of Code 2024
#12/6

import helpers as hp

map = hp.readIn()
tempmap = hp.copylist(map)

hp.pprint(map)

#if there is something in front of you turn right 90 degrees
#otherwise step forward.

pos = []
global dir
steps =[] # This will be a list of the steps including y, x, and dir

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

def turnright():
    global dir
    # print(dir)
    if dir < 3:
        dir += 1
    else:
        dir = 0
    
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

def stamp():
    global looping
    global steps
    # map[pos[0]] = map[pos[0]][:pos[1]] +  "X" + map[pos[0]][pos[1]+1:]
    cur = [pos[0], pos[1], dir]
    if cur in steps:
        print('Looping')
        loopcount += 1
        # return True
    steps.append(cur)
    # return False
    print(steps)

def countpath():
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "X":
                count += 1
    return count

def checkfront():
    global dir
    try:
        if dir == 0 and map[pos[0]-1][pos[1]] == '#':
            # print("bang")
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
        else:
            step()
            stamp()
            return True
    except:
        return False 

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '#' or map[y][x] == '^':
            continue
        else:
            map[y] = map[y][:x] + '#' + map[y][x+1:]
            hp.pprint(map)
            print()
            while checkfront():
                continue
            map[y] = map[y][:x] + '.' + map[y][x+1:]


print(loopcount)
#part 2

