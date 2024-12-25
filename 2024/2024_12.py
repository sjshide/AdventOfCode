from utils import *

inp = get_input(2024,12)

g = grid2dict(inp)
G = nx.Graph()

for x in g:
    G.add_node(x)
for x in g:
    a,b = x
    v = g[x]
    for d in [-1,1]:
        if (a+d,b) in g:
            if g[(a+d,b)]==v:
                G.add_edge(x,(a+d,b))
        if (a,b+d) in g:
            if g[(a,b+d)]==v:
                G.add_edge(x,(a,b+d)) 

A = 0
B = 0
for x in nx.connected_components(G):
    area = len(x)
    perim = sum([4-G.degree(t) for t in x])
    
    A+=area*perim
    
    # B
    # keep track of line and side of edge you're on
    # while edges haven't been checked
    # pick a random point in the edge and work outwards
    # until the edge ends.
    edgePieces = set()
    for (a,b) in x:
        for d in [-1,1]:
            if not (a+d,b) in x:
                edgePieces.add((a,b,d,0))
            if not (a,b+d) in x:
                edgePieces.add((a,b,0,d))
                
    edgeCt=0
    while edgePieces:
        (a,b,d1,d2) = edgePieces.pop()
        i=1
        while (a+i*d2,b+i*d1,d1,d2) in edgePieces:
            edgePieces.remove((a+i*d2,b+i*d1,d1,d2))
            i+=1
        i=1
        while (a-i*d2,b-i*d1,d1,d2) in edgePieces:
            edgePieces.remove((a-i*d2,b-i*d1,d1,d2))
            i+=1        
        edgeCt+=1
        
    B+=(area*edgeCt)   

print('Part A Solution:', A)
print('Part B Solution:', B)