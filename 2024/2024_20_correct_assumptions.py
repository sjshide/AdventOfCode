from utils import *

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
M = nx.shortest_path(G,start,end)

A,B = 0,0 
for d1 in range(len(M)-2):
    (y1,x1) = M[d1]
    for d2 in range(d1+2,len(M)):
        (y2,x2) = M[d2]
        manh = abs(y1-y2)+abs(x1-x2)
        if d2-d1-manh>99:
            if manh<3:
                A+=1
            if manh<21:
                B+=1

print('Part A Solution:', A)
print('Part B Solution:', B)