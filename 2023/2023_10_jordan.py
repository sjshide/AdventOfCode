from utils import *

inp = get_input(2023,10)

grid = grid2dict(inp)

g = nx.DiGraph()

for n in grid:
    g.add_node(n)

# start with a directed version of the graph
# this has (for instance) and L->R edge for '-|'
# but does not have an R->L edge here
for n in grid:
    '''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile. but unknown
    '''
    y,x = n
    if grid[n]=='|':
        g.add_edge(n,(y-1,x))
        g.add_edge(n,(y+1,x))
    if grid[n]=='-':
        g.add_edge(n,(y,x-1))
        g.add_edge(n,(y,x+1))
    if grid[n]=='L':
        g.add_edge(n,(y-1,x))
        g.add_edge(n,(y,x+1))
    if grid[n]=='J':
        g.add_edge(n,(y-1,x))
        g.add_edge(n,(y,x-1))
    if grid[n]=='7':
        g.add_edge(n,(y+1,x))
        g.add_edge(n,(y,x-1))
    if grid[n]=='F':
        g.add_edge(n,(y+1,x))
        g.add_edge(n,(y,x+1))
    if grid[n]=='S':
        g.add_edge(n,(y-1,x))
        g.add_edge(n,(y+1,x))
        g.add_edge(n,(y,x-1))
        g.add_edge(n,(y,x+1))
        start = n

# Get directed cycles in the graph
# this gives an ordering on the cycle from the start
# which will be used for B
cyc = [x for x in nx.simple_cycles(g) if start in x]

# Get the undirected version of the graph where
# reciprocal = True means we require both directions have edges.
# This'll give the actual cycle we want
gDir = g.to_undirected(reciprocal=True)

# The furthest point is at half the length of the connected component of the start node
# (assuming start is in a single cycle, which seems reasonable given problem statement)
cc =  nx.node_connected_component(gDir,start)
A = len(cc)//2

# B
# I did actually think to try Jordan Curve Theorem implementation live,
# but figured it might be too tricky. Then I saw that people made it work,
# so decided to give it a go.

# For each row, calculate times a horizontal ray crosses from the left side
# can think of shifting all horizontal pipes "down" slightly
# so count L, |, J as crossings, but not F, - or 7

# This is super easy...really wish I'd thought for a few more minutes about it

# Update: need to actually handle S and change it to correct pipe for this to work
# Misread output as correct for my test case ... Thanks to Wim for pointing out that this is incorrect
# (although the reason for his version being wrong ended up different from mine)

yS,xS = start
sNbs = gDir.neighbors(start)

pipeMap = {}
pipeMap['dl'] = '7'
pipeMap['dr'] = 'F'
pipeMap['du'] = '|'
pipeMap['lr'] = '-'
pipeMap['lu'] = 'J'
pipeMap['ru'] = 'L'

nbDirs = []
for (y,x) in sNbs:
    if y-yS==1:
        nbDirs.append('d')
    elif y-yS==-1:
        nbDirs.append('u')
    elif x-xS==1:
        nbDirs.append('r')
    elif x-xS==-1:
        nbDirs.append('l')
nbDirs = ''.join(sorted(nbDirs))

grid[start] = pipeMap[nbDirs]

B = 0
for i in range(len(inp)):
    crossings = 0
    for j in range(len(inp[i])):
        if (i,j) in cc:
            if grid[(i,j)] in 'L|J':
                crossings+=1
        elif crossings%2:
            B+=1


print('Part A Solution:', A)
print('Part B Solution:', B)