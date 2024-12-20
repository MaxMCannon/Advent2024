#Advent of Code 2024
#12/7

import helpers as hp
import itertools

calibrations = hp.readIn()
operations = ["+", "x"]

def getcombinations(n):
    return [''.join(combination) for combination in itertools.product([operations[0], operations[1]], repeat=n)]

ops2 = ["+", "x", "|"]

def getcombs2(n):
    return [''.join(combination) for combination in itertools.product([ops2[0], ops2[1], ops2[2]], repeat=n)]
        

def checkcalibration(target, nums, combs):
    runningvalue = nums[0]

    for c in combs:
        for i in range(len(c)):
            if c[i] == '+':
                runningvalue += nums[i+1]
            elif c[i] == 'x':
                runningvalue *= nums[i+1]
        if runningvalue == target:
            return True
        else:
            runningvalue = nums[0]
    return False

def checkwithconcat(target, nums, combs):
    runningvalue = nums[0]
    for c in combs:
        for i in range(len(c)):
            if c[i] == '+':
                runningvalue += nums[i+1]
            elif c[i] == 'x':
                runningvalue *= nums[i+1]
            elif c[i] == '|':
                runningvalue = int(str(runningvalue) + str(nums[i+1])) 
        if runningvalue == target:
            return True
        else:
            runningvalue = nums[0]
    return False

    

# total = 0

# for c in calibrations:
#     target = int(c.split(':')[0])
#     nums = hp.listSTOIdelim(c.split(':')[1], ' ')
#     if checkcalibration(target, nums, getcombinations(len(nums)-1)):
#         total += target
#     # print(target)
#     # print(nums)

# print(total)

total2 = 0 
for c in calibrations:
    target = int(c.split(':')[0])
    nums = hp.listSTOIdelim(c.split(':')[1], ' ')
    if checkwithconcat(target, nums, getcombs2(len(nums)-1)):
        total2 += target
        # print(target)
        # print(nums)

print(total2)