from utils import *

inp = get_input(2024,18)

G = nx.Graph()
for x in range(71):
    for y in range(71):
        G.add_node((y,x))
        
for (y,x) in list(G.nodes):
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (y+dy,x+dx) in list(G.nodes):
            G.add_edge((y,x),(y+dy,x+dx))
                        
for i in range(len(inp)):
    if i==1024:
        A=nx.shortest_path_length(G,(0,0),(70,70))
    x,y = [int(t) for t in inp[i].split(',')]
    if (y,x) in G.nodes:
        G.remove_node((y,x))
    try:
        nx.shortest_path_length(G,(0,0),(70,70))
    except:
        B = inp[i]
        break
        
print('Part A Solution:', A)
print('Part B Solution:', B)