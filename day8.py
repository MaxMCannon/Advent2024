#Advent of Code 2024
#12/8

import helpers as hp

map = hp.readIn()
antinodemap = hp.copylist(map)



hp.pprint(map)
count = 0

def placeantinode(y, x):
    global count
    try:
        if y >= 0 and y <= len(map) and x >= 0 and x <= len(map):
            antinodemap[y] = antinodemap[y][:x] + '#' + antinodemap[y][x+1:]
    except:
        pass
    # if y >= 0 and y <= len(map) and x >= 0 and x <= len(map) and map[y][x] != '.' and map[y][x] != '#':
    #     count += 1

# placeantinode(0,0)
# hp.pprint(map)

def findantenae(symb):
    locs = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symb:
                locs.append([y, x])

    for i in range(len(locs)):
        for j in range(len(locs)):
            if i == j:
                continue
            else:
                # print('placing')
                ydist = locs[i][0]-locs[j][0]
                xdist = locs[i][1]-locs[j][1]
                while locs[i][0]+ydist > 0 and locs[i][0]+ydist <= len(map) and locs[i][1]+xdist> 0 and locs[i][1]+xdist < len(map[0]):
                    placeantinode(locs[i][0]+ydist, locs[i][1]+xdist)
                    ydist -= locs[j][0]
                    xdist -= locs[j][1]
    return locs

def counthash():
    global count
    for y in range(len(map)):
        for x in range(len(map[y])):
            if antinodemap[y][x] == '#':
                count += 1


for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] != '.' and map[y][x] != '#':
            print(findantenae(map[y][x]))

hp.pprint(antinodemap)
counthash()
print(count)
