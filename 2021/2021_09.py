from utils import *
import networkx as nx

inp = get_input(2021,9)

d=dict()
for i in range(len(inp)):
    for j in range(len(inp[i])):
        d[(i,j)]=int(inp[i][j])

    
# A
A = 0

for (i,j) in d:
    nbct = 0
    ct = 0
    for (dy,dx) in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (i+dy,j+dx) in d:
            nbct+=1
            if d[(i+dy,j+dx)]>d[(i,j)]:
                ct+=1
    if ct==nbct:
        A+=(1+d[(i,j)])
    
        
# B
B = 1

G = nx.Graph()

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if d[(i,j)]!=9:
            G.add_node((i,j))

for (i,j) in G:
    for (dy,dx) in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (i+dy,j+dx) in G:
            G.add_edge((i+dy,j+dx),(i,j))


for l in sorted(([len(x) for x in list(nx.connected_components(G))]))[-3:]:
    B*=l  

print('Part A Solution:', A)
print('Part B Solution:', B)