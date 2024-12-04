#Advent of Code 2024 Day 1
#12/2/24
import math as m

ins = open("input.txt").read().splitlines()
l1 = []
l2 = []

for l in ins:
    l1.append(int(l.split()[0]))
    l2.append(int(l.split()[1]))

l1.sort()
l2.sort()

diff = 0

for i in range(len(l1)):
    diff += abs(l1[i]-l2[i])

print("part 1 : " + str(diff))

score = 0
for i in range(len(l1)):
    score += l1[i] * l2.count(l1[i])

print("part2 : " + str(score))
    

# print(l1)
# print(l2)