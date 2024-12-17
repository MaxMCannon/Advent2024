#Advent of Code 2024
#12/6

import helpers as hp

map = hp.readIn()

# hp.pprint(map)

#if there is something in front of you turn right 90 degrees
#otherwise step forward.

pos = []
global dir
steps = [] # This will be a list of the steps including y, x, and dir

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
# print(steps)

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
mainpath = [[starty, startx, dir]]

def setmain():
    global mainpath
    while checkfront():
        step()
        newpos = [pos[0], pos[1], dir]
        mainpath.append(newpos)

setmain()
# 
# print(mainpath)

def checkmap():
    global steps
    global loopcount
    while checkfront():
        step()
        newpos = [pos[0], pos[1], dir]
        if newpos in steps:
            # hp.pprint(map)
            # print(steps)
            loopcount += 1
            print(loopcount)
            steps = []
            return True
        steps.append(newpos)
    # print(steps)
    steps = [[starty, startx, 0]]    
    return False

tested = []
def getrights(y, x, d):
    try:
        points = []
        if d == 0:  
            while map[y][x] != '#':
                points.append([y, x, 1])
                x += 1
        if d == 1:  
            while map[y][x] != '#':
                points.append([y, x, 2])
                y += 1
        if d == 2:  
            while map[y][x] != '#':
                points.append([y, x, 3])
                x -= 1
        if d == 3:  
            while map[y][x] != '#':
                points.append([y, x, 0])
                y -= 1
        print(points)
        return points
    except:
        return None


# print(mainpath)
# for i in range(len(mainpath)):
#     # print(mainpath[i])
#     y = mainpath[i][0]
#     x = mainpath[i][1]
#     d = mainpath[i][2]
#     try:
#         for g in getrights(y, x, d):
#             if g in mainpath[:i]: 
#                 print("found loop")       
#                 loopcount += 1
#                 break
#     except:
#         pass
    # if d == 1:
    #     if [y, x, 2] in getrights(y, x, 0):
    #         print([y, x, 2])
    #         loopcount += 1
    # if d == 2:
    #     if [y, x, 3] in mainpath[:i]:
    #         print([y, x, 3])
    #         loopcount += 1
    # if d == 3:
    #     if [y, x, 0] in mainpath[:i]:
    #         print([y, x, 0])
    #         loopcount += 1

for p in mainpath:
    tempmap = hp.copylist(map)
    y = p[0]
    x = p[1]
    d = p[2]
    temppos = [y, x]
    if temppos in tested:
        continue
    tested.append(temppos)
    if map[y][x] == '^':
        continue
    map[y] = map[y][:x] + '#' + map[y][x+1:]
    # hp.pprint(map)
    # print()
    pos = [y, x]
    dir = d
    checkmap()
    map = hp.copylist(tempmap)


# for y in range(len(map)):
#     for x in range(len(map[y])):
#         tempmap = hp.copylist(map)
#         map[y] = map[y][:x] + '#' + map[y][x+1:]
#         # hp.pprint(map)
#         pos = [starty, startx]
#         dir = 0
#         checkmap()
#         map = hp.copylist(tempmap)

print(loopcount)

