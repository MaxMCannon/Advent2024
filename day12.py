#Advent of Code day 12
import helpers as hp

garden = hp.readIn()

# hp.pprint(garden)

plots = []

def getplots(plant):
    plot = hp.copylist(garden)
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j] != plant:
                plot[i] = plot[i][:j] + '.' + plot[i][j+1:]

    if plot in plots:
        return True
        
    hp.pprint(plot)
    plots.append(plot)

for y in range(len(garden)):
    for x in range(len(garden[y])):
        getplots(garden[y][x])
    
print(plots)
