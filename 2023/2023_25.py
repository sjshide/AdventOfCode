from utils import *

# Seems like the theme of this year was abusing networkx methods
# Live: I printed the graph 
# nx.draw_spectral(G,with_labels=True)
# which has the nice property that clusters really stand out
# I then manually removed the 3 obvious edges and did the computation
# Turns out (as I figured existed but wasn't able to figure out the correct name)
# there is just a method for this.

# Still went 165/150 global but probably really should've leaderboarded...too out of practice

inp = get_input(2023,25)

G = nx.Graph()
for x in inp:
    node, con = x.split(': ')
    for c in con.split(' '):
        G.add_edge(node, c)
        
mec = nx.minimum_edge_cut(G)
for x in mec:
    G.remove_edge(x[0],x[1])
                  
cc = list(nx.connected_components(G))             
A = len(cc[0])*len(cc[1])                                
                  
print('Part A Solution:', A)
print('Part B Solution:', 'PUSH THE BUTTON!')