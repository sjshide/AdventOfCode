from utils import *
from collections import Counter

# originally for B I thought you had to stay in the #s once you entered.
# wasted a bunch of time trying to figure this out.
# eventually actually looked at the examples and saw this wasn't the case
# actually the manhattan distance approach did occur to me, but 
# thought it wouldn't work for the above reason.
# I guess I should rewrite with that approach too, but this is what I used live
# pretty inelegant

inp = get_input(2024,20)

g = grid2dict(inp)
G = nx.Graph()
for x in g:
    if g[x]!='#':
        G.add_node(x)
        if g[x]=='S':
            start = x
        if g[x]=='E':
            end = x
            
for (y,x) in list(G.nodes):
    for (dy,dx) in [(-1,0),(1,0),(0,1),(0,-1)]:
        if (y+dy,x+dx) in g and g[(y+dy,x+dx)]!='#':
            G.add_edge((y,x),(y+dy,x+dx)) 

# get how far each node is into the path
p = nx.shortest_path(G,start,end)
stepG = dict()
for i in range(len(p)):
    stepG[p[i]]=i
    
def calcCheats(delta):
    d = dd(list)
    for (Y,X) in stepG:
        thisStep = stepG[(Y,X)]
        visited = set()
        visited.add((Y,X))
        nbs = set()
        nbs.add((Y,X))
        for step in range(delta):
            newNbs = set()
            for (y,x) in nbs:
                for (dy,dx) in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nY = y+dy
                    nX = x+dx
                    if (nY,nX) in g and (nY,nX) not in visited:
                        newNbs.add((nY,nX))
                        if (nY,nX) in stepG:
                            d[(Y,X,nY,nX)].append(stepG[(nY,nX)]-stepG[(Y,X)]-step-1)
            nbs=newNbs
            visited.update(nbs)
    ct = sorted([max(d[t]) for t in d])       
    c = Counter(ct)
    return(sum([c[x] for x in c if x>=100]))         
    
A = calcCheats(2)
B = calcCheats(20)

print('Part A Solution:', A)
print('Part B Solution:', B)