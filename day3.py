#Advent 2024
#12/3
import helpers as hp

ins = open("input.txt").read()

remainder = ''
remainder = ins.split()
# print(ins.split('mul('))
lists = ins.split('mul(')

def getmult(s):
    # print(s)
    if not s[0].isnumeric():
        return 0
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        if s[i] == ',':
            continue
        if s[i] != ')':
            return 0
        # if not s[i].isnumeric() or s[i] != ',':
        #     print(s[i])
        #     if s[i] != ")":
        #         return 0
    # print(int(s.split(',')[0])*int(s.split(',')[1]))
    return int(s.split(',')[0])*int(s.split(',')[1])

sum = 0
for l in lists:
    sum += getmult(l.split(')')[0])
        
print("Part 1: " + str(sum))

## part 2

# def multiply

do = True
newsum = 0

for i in range(len(ins)):
    # print(ins[i:i+6])
    # print('don\'t')
    if ins[i:i+7] == 'don\'t()':
        do = False
    if do:
        if ins[i:i+4] == 'mul(':
            # print(ins[i+4:])
            newsum += getmult(ins[i+4:].split(')')[0])
            # print("found")
    elif ins[i:i+4] == 'do()':
        do = True

print("Part 2 : " + str(newsum))