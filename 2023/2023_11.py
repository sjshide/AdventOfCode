from utils import *

inp = get_input(2023,11)

grid  = grid2dict(inp)
galaxies = [x for x in grid if grid[x]=='#']

emptyRows = []
emptyCols = []

for i in range(len(inp)):
    if set(inp[i])=={'.'}:
        emptyRows.append(i)
for i in range(len(inp[0])):
    if set([inp[j][i] for j in range(len(inp))])=={'.'}:
        emptyCols.append(i)
        
def dist(g1,g2,mult):
    y1,x1 = g1
    y2,x2 = g2
    
    initD = abs(y1-y2)+abs(x1-x2)
    
    for t in emptyRows:
        if t in range(min(y1,y2),max(y1,y2)):
            initD+=(mult-1)
    for t in emptyCols:
        if t in range(min(x1,x2),max(x1,x2)):
            initD+=(mult-1)
    return(initD)

A, B = 0, 0
for g1 in galaxies:
    for g2 in galaxies:
        A+=dist(g1,g2,2)
        B+=dist(g1,g2,1000000)


print('Part A Solution:',A//2)
print('Part B Solution:',B//2)