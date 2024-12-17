#Advent of Code 2024
#12/7

import helpers as hp
import itertools

calibrations = hp.readIn()
operations = ["+", "x"]

def getcombinations(n):
    return [''.join(combination) for combination in itertools.product([operations[0], operations[1]], repeat=n)]
        
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
    

total = 0

for c in calibrations:
    target = int(c.split(':')[0])
    nums = hp.listSTOIdelim(c.split(':')[1], ' ')
    if checkcalibration(target, nums, getcombinations(len(nums)-1)):
        total += target
    print(target)
    print(nums)

print(total)