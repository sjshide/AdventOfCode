from utils import *

inp = get_input(2024,8)

g = grid2dict(inp)
revG = dd(list) 
for x in g:
    revG[g[x]]+=[x]

locsA = set()
locsB = set()
for freq in revG:
    if freq!='.':
        l = revG[freq]
        for i in range(len(l)-1):
            y1,x1 = l[i]
            for j in range(i+1,len(l)):
                y2,x2 = l[j]
                dy = y1-y2
                dx = x1-x2
                # overkill lol but w/e
                for k in range(-100,100): 
                    c = (y2+k*dy,x2+k*dx)
                    if c in g:
                        locsB.add(c)
                        if k in [-1,2]:
                            locsA.add(c)
                                      
print('Part A Solution:', len(locsA))
print('Part B Solution:', len(locsB))