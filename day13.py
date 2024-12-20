#Advent Day 13
#12/16

import helpers as hp

raw = hp.readIn()

# hp.pprint(raw)

#Mapping the buttons and prizes to look like [[Ax, Ay], [Bx, By], [Px, Py]]
machines = []

A = []
B = []
P = []

addedprize = 10000000000000

for r in raw:
    if r == '':
        machines.append([A, B, P])
        A = []
        B = []
        P = []
    if 'A:' in r:
        A.append(int(r.split('X+')[1].split(', ')[0]))
        A.append(int(r.split('Y+')[1]))
    if 'B:' in r:
        B.append(int(r.split('X+')[1].split(', ')[0]))
        B.append(int(r.split('Y+')[1]))
    if 'Prize' in r:
        P.append(int(r.split('X=')[1].split(', ')[0])+ addedprize)
        P.append(int(r.split('Y=')[1]) + addedprize)
    
machines.append([A, B, P])
# hp.pprint(machines)

def playmachine(machine):
    print(machine)
    A = machine[0]
    B = machine[1]
    P = machine[2]
    n = (P[0]*B[1]-B[0]*P[1])/(A[0]*B[1]-B[0]*A[1])
    m = (P[1]*A[0]-A[1]*P[0])/(A[0]*B[1]-B[0]*A[1])
    if n == int(n) and m == int(m):
        return int(3 * n + m)
    else:
        return 0
    # for n in range(101):
    #     for m in range(101):
    #         if ((n*A[0]) + (m*B[0]) == P[0]) and ((n*A[1]) + (m*B[1]) == P[1]):
    #             wins.append([n, m])
    # if len(wins) == 0:
    #     return 0
    # mincost = wins[0][0] * 3 + wins[0][1]
    # for w in wins: 
    #     if w[0] * 3 + w[1] < mincost:
    #         mincost = w[0] * 3 + w[1]
    # print(wins)
    # return mincost

# playmachine(machines[0])

total = 0
for mach in machines:
    total += playmachine(mach)
print(total)


