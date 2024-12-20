#Advent day 11
#Rules
#if the stone is engraved 0, it becomes 1
#if the stone has even digits, it splits into two, left half , right half
#   Dont keep leading zeros
#else: multiply by 2024

import helpers as hp

stones = open('input.txt').read().split(' ')

print(stones)

def blink():
    tempstones = []
    for i in range(len(stones)):
        if stones[i] == '0':
            tempstones.append('1')
        elif len(stones[i]) % 2 == 0: 
            h1 = stones[i][:int(len(stones[i])/2)]
            h2 = stones[i][int(len(stones[i])/2):]
            if int(h1) == 0:
                tempstones.append('0')
            else:
                tempstones.append(h1.lstrip('0'))
            if int(h2) == 0:
                tempstones.append('0')
            else:
                tempstones.append(h2.lstrip('0'))

        else:
            tempstones.append(str(int(stones[i])*2024))
    return tempstones

def cleanstones():
    cleanstones = []
    for s in stones:
        if int(s) == 0:
            cleanstones.append('0')
        elif s != '0':
            cleanstones.append(s.lstrip('0'))
    return cleanstones

stonesperblink = [len(stones)]
target = 6

for i in range(target):
    print((i/target)*100)
    stones = blink()
    stonesperblink.append(len(stones))
    # stones = cleanstones()
    # print(stones)

print(stonesperblink)

print(len(stones))