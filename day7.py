#Advent of Code 2024
#12/7

import helpers as hp

calibrations = hp.readIn()

def checkcalibration(target, nums):
    

for c in calibrations:
    target = int(c.split(':')[0])
    nums = hp.listSTOIdelim(c.split(':')[1], ' ')
    print(target)
    print(nums)