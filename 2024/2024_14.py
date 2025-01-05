from utils import *

'''
Live, had the (apparently) correct intuition that the correct 
layout would be the first one where each robot was in a unique positions.
Then I coded it wrong...

Ended up scrolling through ~3k of the pictures until I found the right one.

Here, using the (apparent) fact that the correct layout has the lowest safety factor, which also probably should've been a reasonable guess for how to approach. 
'''

inp = get_input(2024,14)

robots = []
maxX = 101
maxY = 103
for i in range(len(inp)):
    x = inp[i]
    p,v = x.split(' ');
    px,py = [int(t) for t in p[2:].split(',')]
    vx,vy = [int(t) for t in v[2:].split(',')]
    robots.append([px,py,vx,vy])

    
minSF = pow(10,10) 
bestI = -1
bestPlot = []
for sec in range(101*103):
    rlocs = dd(int)
    for px,py,vx,vy in robots:
        newP = ((px+sec*vx)%maxX,(py+sec*vy)%maxY)
        rlocs[newP]+=1
    s00,s01,s10,s11 = 0,0,0,0    
    for (x,y) in rlocs:
        if 2*x<maxX-1:
            if 2*y<maxY-1:
                s00+=rlocs[(x,y)]
            elif 2*y>maxY-1:
                s01+=rlocs[(x,y)]
        elif 2*x>maxX-1:
            if 2*y<maxY-1:
                s10+=rlocs[(x,y)]
            elif 2*y>maxY-1:
                s11+=rlocs[(x,y)]
    sf = s00*s01*s10*s11
    if sec==100:
        A=sf
    elif sf<minSF:
        minSF = sf
        bestI = sec
        bestPlot = []    
        for y in range(maxY):
            s = ''
            for x in range(maxX):
                if (x,y) not in rlocs:
                    s+=' '
                else:
                    s+='*'
            bestPlot.append(s)
        
    
        
        



print('Part A Solution:', A)
print('Part B Solution:', bestI)

for s in bestPlot:
    print(s)