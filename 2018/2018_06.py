from utils import *

inp = get_input(2018,6)


### not thinking very hard about guarantees around going outside the obvious convex hull
### so these might not work in general? when coding used bigger bounds to be more sure.
### bounds below work for my input

### pretty slow regardless. lots of room to optimize here

pts = set()
for this in inp:
    (y,x) = [int(t) for t in this.split(', ')]
    pts.add((y,x))

    
miny = min(t[0] for t in pts)
maxy = max(t[0] for t in pts)
minx = min(t[1] for t in pts)
maxx = max(t[1] for t in pts)


def manh(x1,y1,x2,y2):
    return(abs(x1-x2)+abs(y1-y2))

opts = [1,2]
cts = dict()

for bdry in opts:
    grid = dict()
    for i in range(-minx-bdry,maxx+bdry):
        for j in range(-miny-bdry,maxy+bdry):

            best_id = -1
            closest_dist = pow(10,10)
            tie = 0

            for (y,x) in pts:

                if manh(y,x,i,j)<closest_dist:
                    best_id = (y,x)
                    closest_dist=manh(y,x,i,j)
                    tie=0
                elif manh(y,x,i,j)==closest_dist:
                    tie=1
                    best_id = '.'

            grid[(i,j)] = best_id
            
    cts[bdry]=[([grid[asdf] for asdf in grid].count(t),t) for t in pts]

A = max([t[0] for t in set(cts[opts[0]]).intersection(set(cts[opts[1]]))])


#B
def tot_dist(y,x):
    tot = 0
    for (i,j) in pts:
        tot+=manh(y,x,i,j)
    return(tot)

#idk big just to be careful
B = 0
for i in range(-miny,maxy):
    for j in range(-minx,maxx):
        if tot_dist(i,j)<10_000:
            B+=1


print('Part A Solution:', A)
print('Part B Solution:', B)