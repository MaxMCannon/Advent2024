def readIn():
    return open("input.txt").read().splitlines()

def listSTOI(l):
    return [int(x) for x in l]

def copylist(l):
    out = []
    for i in l:
        out.append(i)
    return out

def reverseList(l):
    out = []
    for i in range(len(l)-1, -1, -1):
        out.append(l[i])
    return out

def pprint(l):
    for n in l:
        print(n)


#to build:
#Create 2d grid from dimensions
#check around 4x
#check around 8x
#