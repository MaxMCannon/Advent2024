#advent 2024
#12/5

import helpers as hp


rules = hp.readIn()
updates = []

appending = False
splitidx = 0
for i in range(len(rules)):
    if rules[i] == '':
        splitidx = i



updates = rules[splitidx+1:]
rules = rules[:splitidx]
updatedrules = []
for r in rules: 
    updatedrules.append([int(r[:2]), int(r[3:])])

for u in updates: 
    u = hp.listSTOIcommas(u)
    

def testupdates(update):
    # print(update)
    for i in range(len(update)):
        for r in updatedrules:
            if update[i] == r[0] and r[1] in update[:i]:
                return False
 
    return True

sum = 0

for u in updates:
    u = hp.listSTOIcommas(u)
    if testupdates(u):
        # print(u[int(len(u)/2)])
        sum += u[int(len(u)/2)]
    
print(sum)
# hp.pprint(updatedrules)
# hp.pprint(updates)

newlist = []
newsum = 0

for u in updates:
    u = hp.listSTOIcommas(u)
    if not testupdates(u):
        newlist.append(u)

for u in newlist:
    while not testupdates(u):
        for i in range(len(u)):
            for r in updatedrules:
                if u[i] == r[0] and r[1] in u[:i]:
                    hp.swapListElements(u, r[0], r[1])
    print(u)

for u in newlist:
    newsum += u[int(len(u)/2)]
print(newsum)