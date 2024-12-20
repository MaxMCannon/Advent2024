#Advent of code day 17
#12/17
import helpers as hp
import math
import time

start_time = time.time()

raw = open('input.txt').read().splitlines()

A = 0
B = 0
C = 0
program = []
pointer = 0
output = []

for r in raw:
    if 'A: ' in r:
        A = int(r.split(': ')[1])
    if 'B: ' in r:
        B = int(r.split(': ')[1])
    if 'C: ' in r:
        C = int(r.split(': ')[1])
    if 'Program' in r:
        program = hp.listSTOIdelim(r.split(': ')[1], ',')

def getcombo(op):
    if op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C
    else:
        return False

# def itob(n):
#     return "{0:b}".format(n)

# def btoi(n):
#     return int(n, 2)

def adv(op): #0
    global A
    A = math.trunc(A/(math.pow(2, getcombo(op))))

def bxl(op): #1
    global B
    out = B ^ op
    B = out
    return out

def bst(op): #2
   global B
   B = getcombo(op) % 8 
   return B

def jnz(op): #3 - to do - don't move pointer f jnz
    global pointer
    if A == 0:
        return True
    else:
        pointer = op

def bxc(op): #4
    global B
    global C
    B = B ^ C
    return B

def out(op): #5
    global output
    output.append(getcombo(op) % 8)
    # print(output)

def bdv(op): #6
    global B
    B = math.trunc(A/(math.pow(2, getcombo(op))))

def cdv(op): #7
    global C
    C = math.trunc(A/(math.pow(2, getcombo(op))))

#part 1 \/\/\/

# while pointer < len(program):
#     ins = program[pointer]
#     op = program[pointer + 1]
#     if ins == 0:
#         adv(op)
#         pointer += 2 
#     elif ins == 1:
#         bxl(op)
#         pointer += 2 
#     elif ins == 2:
#         bst(op)
#         pointer += 2 
#     elif ins == 3:
#         if A == 0:
#             break
#         jnz(op)
#     elif ins == 4:
#         bxc(op)
#         pointer += 2 
#     elif ins == 5:
#         out(op)
#         pointer += 2 
#     elif ins == 6:
#         bdv(op)
#         pointer += 2 
#     elif ins == 7:
#         cdv(op)
#         pointer += 2

def checkout(): 
    for i in range(len(output)):
        if output[i] != program[i]:
            return False
    return True

startA = A
multiplier = 1
while output != program:
    pointer = 0
    output = []
    A = startA + multiplier
    print(A)
    while pointer < len(program) and checkout():
        ins = program[pointer]
        op = program[pointer + 1]
        if ins == 0:
            adv(op)
            pointer += 2 
        elif ins == 1:
            bxl(op)
            pointer += 2 
        elif ins == 2:
            bst(op)
            pointer += 2 
        elif ins == 3:
            if A == 0:
                break
            jnz(op)
        elif ins == 4:
            bxc(op)
            pointer += 2 
        elif ins == 5:
            out(op)
            pointer += 2 
        elif ins == 6:
            bdv(op)
            pointer += 2 
        elif ins == 7:
            cdv(op)
            pointer += 2
    # print(output)
    # print(len(output))
    multiplier += 1


    
print("A : " + str(A))
print("B : " + str(B))
print("C : " + str(C))
print('output : ' + str(output))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
