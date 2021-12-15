from utils import *

import networkx as nx

## Grateful for networkx

inp = get_input(2021,15)


d_A = grid2dict(inp)

for x in d_A:
    d_A[x]=int(d_A[x])
    
d_B = dict()

for i in range(5):
    for j in range(5):
        for (y,x) in d_A:
            guess = (int(d_A[(y,x)]) + (i+j))
            if guess>=10:
                guess-=9        
            d_B[(y+100*i,x+100*j)] = guess
        
def solve(d):
    G = nx.DiGraph()
    for key in d:
        G.add_node(key)
        
    for (y,x) in G.nodes():
        nbs = []
        if (y-1,x) in G:
            nbs.append((y-1,x))
        if (y+1,x) in G:
            nbs.append((y+1,x))
        if (y,x-1) in G:
            nbs.append((y,x-1))
        if (y,x+1) in G:
            nbs.append((y,x+1))

        for node in nbs:
            G.add_edge((y,x),node,weight=d[node])
        
    M = int(pow(len(d),.5))-1
    
    best_path = nx.algorithms.shortest_paths.weighted.dijkstra_path(G,(0,0),(M,M))
    wt = 0
    for x in best_path[1:]:
        wt+=d[x]
    return(wt)
    

print('Part A Solution:', solve(d_A))
print('Part B Solution:', solve(d_B))