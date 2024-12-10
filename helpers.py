def readIn():
    return open("input.txt").read().splitlines()

def listSTOI(l):
    return [int(x) for x in l]

def copylist(l):
    out = []
    [out.append(i) for i in l]
    return out

def reverseList(l):
    out = []
    for i in range(len(l)-1, -1, -1):
        out.append(l[i])
    return out

def pprint(l):
    for n in l:
        print(n)

def listSTOIdelim(l, delim):
    strs = l.split(delim)
    # print(strs)
    dig = []
    for s in strs:
        if not s.isnumeric():
            continue
        dig.append(int(s))
    return dig

def swapListElements(l, e1, e2):
    outlist = []
    i1 = 0
    i2 = 0
    for i in range(len(l)):
        if l[i] == e1:
            i1 = i
        if l[i] == e2:
            i2 = i
    l[i1], l[i2] = l[i2], l[i1]
    return l

    

#to build:
#Create 2d grid from dimensions
#check around 4x
#check around 8x
#