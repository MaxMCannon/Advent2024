#advent of Code 2024
#12/4

import helpers as hp

words = hp.readIn()

# hp.pprint(words)

global count

def buildwords(y, x):
    # The goal is to build 8 words from every direction out of the current position
    # if the word is longer than 4 letters and starts with XMAS, add 1 xmas
    wordlist = []
    tempword = words[y][x]
    currY = y
    currX = x
    counts = 0
    # print(tempword)
    for i in range(8):
        if i == 0:
            while currY > 0 and currX > 0:
                currY -= 1
                currX -= 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 1:
            while currY > 0:
                currY -= 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 2:
            while currY > 0 and currX < len(words[0])-1:
                currY -= 1
                currX += 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 3:
            while currX < len(words[0])-1:
                currX += 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 4:
            while currY < len(words) - 1 and currX < len(words[0]) - 1:
                currY += 1
                currX += 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 5:
            while currY < len(words) -1:
                currY += 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 6:
            while currY < len(words)-1 and currX > 0:
                currY += 1
                currX -= 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
        if i == 7:
            while currX > 0:
                currX -= 1
                tempword += words[currY][currX]
            wordlist.append(tempword)
            currY = y
            currX = x
            tempword = words[y][x]
    print(wordlist)
    for w in wordlist:
        # print(w[0:4])
        if len(w) > 4 and w[0:4] == "XMAS":
            print(w[0:4])
            counts += 1
    return counts

globalcount = 0

for i in range(len(words)):
    for j in range(len(words[i])):
        globalcount += buildwords(i, j)

print(globalcount)

