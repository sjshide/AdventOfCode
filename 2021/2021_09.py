from utils import *
import networkx as nx

inp = get_input(2021,9)

G = nx.Graph()

A = 0
B = 1

for i in range(len(inp)):
    for j in range(len(inp)):
        G.add_node((i,j))
        
for (i,j) in G:
    ct = 0
    nbct = 0
    for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if (i+di,j+dj) in G:
            G.add_edge((i+di,j+dj),(i,j))
            nbct+=1
            if inp[i+di][j+dj]>inp[i][j]:
                ct+=1
    if ct==nbct:
        A+=(1+int(inp[i][j]))

        
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j]=='9':
            G.remove_node((i,j))
            
for l in sorted(([len(x) for x in list(nx.connected_components(G))]))[-3:]:
    B*=l

print('Part A Solution:', A)
print('Part B Solution:', B)