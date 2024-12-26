from utils import *

inp = get_input(2024,23)
G = nx.Graph()
for x in inp:
    a,b = x.split('-')
    G.add_node(a)
    G.add_node(b)
    G.add_edge(a,b)
    
# A
nbs = dd(set)
for (x,y) in G.edges():
    nbs[x].add(y)
    nbs[y].add(x)
    
A=0
for (x,y) in G.edges():
    for z in nbs[x].intersection(nbs[y]):
        if 't' in x[0]+y[0]+z[0]:
            A+=1
A=A//3 # we triple count above
            
# B
t = [x for x in nx.find_cliques(G)]
largest = sorted(t,key=len)[-1]  
s = ''
for x in sorted(largest):
    s+=(x+',')

print('Part A Solution:', A)
print('Part B Solution:', s[:-1])