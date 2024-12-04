#Advent 2024
#12/2
import helpers as hp

reports = hp.readIn()

def checkreport(rep):
    # print(rep)
    temp = hp.reverseList(rep)

    if sorted(rep) != rep and sorted(rep) != temp:
        return False
    for i in range(1, len(rep)):
        if abs(rep[i]-rep[i-1]) > 3 or abs(rep[i]-rep[i-1]) < 1:
            return False
    return True

def checkTwo(rep):
    print(rep)
    temp = []
    for i in range(len(rep)):
        for j in range(len(rep)):
            if j != i:
                temp.append(rep[j])
        print(temp)
        if checkreport(temp):
            return True
        temp = []
    # temp = hp.copylist(rep)
    # for i in range(len(rep)):
    #     print(temp.pop(temp[i]))
    #     if checkreport(temp.pop(temp[i])):
    #         return True
    #     temp = hp.copylist(rep)
    # return False

countsafe = 0

for r in reports:
    r = hp.listSTOI(r.split())
    # print(r)
    if checkreport(r):
        countsafe += 1
    # print(checkreport(r))

print("Part 1: " + str(countsafe))

countsafe2 = 0

for r in reports:
    r = hp.stoi(r.split())
    # print(r)
    if checkreport(r):
        countsafe2 += 1
        continue
    elif checkTwo(r):
        countsafe2 += 1

    # print(checkreport(r))

print("Part 2: " + str(countsafe2))