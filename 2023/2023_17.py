from utils import *

inp = get_input(2023,17)
g = grid2dict(inp)
for x in g:
    g[x]=int(g[x])

# Create a big graph with position + direction info
# encode travel restrictions in edges
# Then use nx.shortest_path
# kinda slow but whatever

# A
G = nx.DiGraph()

# add nodes
for (y,x) in g:
    for level in range(1,4):
        G.add_node((y,x,level,0,0,0))
        G.add_node((y,x,0,level,0,0))
        G.add_node((y,x,0,0,level,0))
        G.add_node((y,x,0,0,0,level))

# add edges
for n in G.nodes:
    y,x,U,L,D,R = n
    # Up
    if (y-1,x) in g and not D and U<3:
        G.add_edge(n,(y-1,x,U+1,0,0,0),weight=g[(y-1,x)])
    # Left
    if (y,x-1) in g and not R and L<3:
        G.add_edge(n,(y,x-1,0,L+1,0,0),weight=g[(y,x-1)])  
    # Down
    if (y+1,x) in g and not U and D<3:
        G.add_edge(n,(y+1,x,0,0,D+1,0),weight=g[(y+1,x)])
    # Right
    if (y,x+1) in g and not L and R<3:
        G.add_edge(n,(y,x+1,0,0,0,R+1),weight=g[(y,x+1)])         

# Start, end
G.add_node((0,0))
G.add_node((140,140))

G.add_edge((0,0),(1,0,0,0,1,0),weight=g[(1,0)])
G.add_edge((0,0),(0,1,0,0,0,1),weight=g[(0,1)])

for n in G:
    y,x = n[:2]
    if (y,x)==(140,140):
        G.add_edge(n,(140,140),weight=0)

t = nx.shortest_path(G,source=(0,0),target=(140,140),weight='weight')
A = 0
for i in range(len(t)-1):
    A+=G.get_edge_data(t[i],t[i+1])['weight']
    
    
# B - same thing but bigger and more conditions
G = nx.DiGraph()

# add nodes
for (y,x) in g:
    for level in range(1,11):
        G.add_node((y,x,level,0,0,0))
        G.add_node((y,x,0,level,0,0))
        G.add_node((y,x,0,0,level,0))
        G.add_node((y,x,0,0,0,level))

# add edges
for n in G.nodes:
    y,x,U,L,D,R = n
    
    # Up
    if (y-1,x) in g and not D and U<10 and (U>0 or L>3 or R>3):
        G.add_edge(n,(y-1,x,U+1,0,0,0),weight=g[(y-1,x)])
    # Left
    if (y,x-1) in g and not R and L<10 and (L>0 or U>3 or D>3):
        G.add_edge(n,(y,x-1,0,L+1,0,0),weight=g[(y,x-1)])  
    # Down
    if (y+1,x) in g and not U and D<10 and (D>0 or L>3 or R>3):
        G.add_edge(n,(y+1,x,0,0,D+1,0),weight=g[(y+1,x)])
    # Right
    if (y,x+1) in g and not L and R<10 and (R>0 or U>3 or D>3):
        G.add_edge(n,(y,x+1,0,0,0,R+1),weight=g[(y,x+1)]) 

# Start, end
G.add_node((0,0))
G.add_node((140,140))

G.add_edge((0,0),(1,0,0,0,1,0),weight=g[(1,0)])
G.add_edge((0,0),(0,1,0,0,0,1),weight=g[(0,1)])

for n in G:
    y,x = n[:2]
    if (y,x)==(140,140):
        G.add_edge(n,(140,140),weight=0)

t = nx.shortest_path(G,source=(0,0),target=(140,140),weight='weight')
B = 0
for i in range(len(t)-1):
    B+=G.get_edge_data(t[i],t[i+1])['weight']
    
print('Part A Solution:', A)
print('Part B Solution:', B)