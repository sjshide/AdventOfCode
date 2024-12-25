from utils import *

inp = get_input(2024,16)

# networkx bash let's go

# layer for each direction, penalize turning at 1000
G = nx.DiGraph()
g = grid2dict(inp)

for x in g:
    if g[x]!='#':
        G.add_node((x,(0,1)))
        G.add_node((x,(0,-1)))
        G.add_node((x,(-1,0)))
        G.add_node((x,(1,0)))
    if g[x]=='S':
        start=x
    if g[x]=='E':
        end=x
        
for (n,d) in list(G.nodes):
    y, x = n
    dy, dx = d
    if (y+dy,x+dx) in g:
        G.add_edge((n,d),((y+dy,x+dx),d),weight=1)
    G.add_edge((n,d),(n,(dx,dy)),weight=1000)
    G.add_edge((n,d),(n,(-dx,-dy)),weight=1000)
        
G.add_node('E')

G.add_edge((end, (1,0)),'E',weight=0)
G.add_edge((end, (-1,0)),'E',weight=0)
G.add_edge((end, (0,1)),'E',weight=0)
G.add_edge((end, (0,-1)),'E',weight=0)

# Start facing right
p=nx.shortest_path(G,(start,(0,1)),'E','weight')
A = 0
for i in range(len(p)-1):
    A+=G.get_edge_data(p[i],p[i+1])['weight']

p=nx.all_shortest_paths(G,(start,(0,1)),'E','weight')   
sB = set()
for x in p:
    for l in x:
        sB.add(l[0])
    
print('Part A Solution:', A)
print('Part B Solution:', len(sB)-1) #account for 'E' node