#Advent of Code day 14
#12/18
import helpers as hp

robots = hp.readIn()

hp.pprint(robots)

ps = []
vs = []
for r in robots:
    ps.append(hp.listSTOI(r.split(' ')[0].split('=')[1].split(',')))
    vs.append(hp.listSTOI(r.split(' ')[1].split('=')[1].split(',')))

# print(ps)
# print(vs)

map = []
spacey = 7
spacex = 11

for y in range(spacey):
    row = []
    for x in range(spacex):
        row.append(0)
    map.append(row)

hp.pprint(map)