from utils import *

inp = get_input(2023,21)

# Gross
# This obviously should have quadratic growth
# And I computationally observed live that in the example the growth
# was polynomial for residue classes mod 2*11 (2 * the width of the grid)
# Spent a ton of time trying to write down an actual expression,
# then realized I could just compute the first several values explicitly
# although this is crazy slow, it gets there...

# nxn copy of the grid
def multgrid(inp,n):
    oneRow = []
    new = []
    for i in range(len(inp)):
        this = inp[i]*n
        oneRow.append(this)
    for _ in range(n):
        new = new+oneRow
    return(new)

# 9 copies is enough to get correct values 
# for 65, 327, 589 (65+2*i*131 for i=0,1,2)
inp = multgrid(inp,9)

g=grid2dict(inp)

startL = [n for n in g if g[n]=='S']
start=startL[len(startL)//2]

G = nx.Graph()
for n in g:
    if g[n] in 'S.':
        G.add_node(n)
for (y,x) in G.nodes():
    for (dy,dx) in [(-1,0),(1,0),(0,1),(0,-1)]:
            if (y+dy,x+dx) in G.nodes():
                G.add_edge((y,x),(y+dy,x+dx))
                
t = nx.single_source_shortest_path_length(G,start)  

# A
A = 0
for x in t:
    if t[x]<=64 and not t[x]%2:
        A+=1

# B
# Live I just plugged this into Wolfram Alpha
# Here let's actually write down the Lagrange interpolation...
xs = []
ys = []
for i in range(0,6,2):
    k = 65+131*i
    o = 0
    for x in t:
        if t[x]<=k and t[x]%2:
            o+=1
    xs.append(i)
    ys.append(o)
    
total = 0
desired = (26501365-65)//131
for i in range(len(xs)):
    denom = 1
    s = 0
    p = 1
    for j in range(len(xs)):
        if i!=j:
            denom*=(xs[i]-xs[j])
            s += xs[j]
            p *= xs[j]
    total+=ys[i]*(desired**2 - s*desired + p)//denom
    
print('Part A Solution:', A)
print('Part B Solution:', total)