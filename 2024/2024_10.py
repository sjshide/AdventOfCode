from utils import *

inp = get_input(2024,10)

g = grid2dict(inp)
for x in g:
    g[x]= int(g[x])
    
G = nx.DiGraph()

starts = [];
ends = [];

for x in g:
    G.add_node(x)
    if g[x]==0:
        starts+=[x]
    if g[x]==9:
        ends+=[x] 
for (y,x) in g:
    for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if (y+dy,x+dx) in g:
            if g[(y+dy,x+dx)]==g[(y,x)]+1:
                G.add_edge((y,x),(y+dy,x+dx))

# like seemingly everyone, I calculated B answer for A initially
# made submission for B quite easy
A = 0
B = 0
for s in starts:
    for e in ends:
        check=0
        for p in nx.all_simple_paths(G,s,e):
            B+=1
            check=1
        A+=check

print('Part A Solution:', A)
print('Part B Solution:', B)