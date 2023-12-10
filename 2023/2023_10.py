from utils import *

# Likely there are much cleaner ways to do this, but it worked
# took me roughly 1.5 hrs

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

# Get the directed version of the graph where
# reciprocal = True means we require both directions have edges.
# This'll give the actual cycle we want
gDir = g.to_undirected(reciprocal=True)

# The furthest point is at half the length of the connected component of the start node
# (assuming start is in a single cycle, which seems reasonable given problem statement)
A = len(nx.node_connected_component(gDir,start))//2

# B
# Idea: traverse the cycle, and keep track of whether
# nodes are to the left or right of the traversal.
# one of these will be inside and the other will be outside

# first, get the directed cycle we'll traverse.
# should be 2 of these in cyc, so pick one
for x in cyc:
    if len(x)==A*2:
        dirCyc = x
        break

# Store info about inside/outside loop for nodes of the graph
# default to ' ' for making printed output more legible
# to check that stuff is working right
inout = dd(lambda: ' ')

# for nodes in the cycle, mark with '.'
for x in dirCyc:
    inout[x]='.'
    
# function to add inside/outside info for unchecked nodes
def checkAdd(y,x,direction):
    if (y,x) not in inout or inout[(y,x)]==' ':
        inout[(y,x)] = direction

        
# Traverse the cycle, keeping track of direction of movement
# mark unseen nodes to the left of movement with 'L'
# and unseen nodes to the right of movement with 'R'
for i in range(1,len(dirCyc)-1):
    (lasty,lastx) = dirCyc[i-1]
    (cy,cx) = dirCyc[i]
    (nexty,nextx) = dirCyc[i+1]

    test = (nexty-lasty,nextx-lastx)
    
    # Can definitely be made more compact...
    if test==(2,0):
        # moving down
        checkAdd(cy,cx-1,'R')
        checkAdd(cy,cx+1,'L')

    if test==(-2,0):
        # moving up
        checkAdd(cy,cx-1,'L')
        checkAdd(cy,cx+1,'R')
            
    if test==(0,2):
        # moving right
        checkAdd(cy-1,cx,'L')
        checkAdd(cy+1,cx,'R')

    if test==(0,-2):
        # moving left
        checkAdd(cy-1,cx,'R')
        checkAdd(cy+1,cx,'L')
   
            
    if test==(-1,1):
        # turn left/up or up/right:
        checkAdd(cy+1,cx,'R')
        checkAdd(cy+1,cx+1,'R')
        checkAdd(cy,cx+1,'R')
        checkAdd(cy-1,cx,'L')
        checkAdd(cy-1,cx-1,'L')
        checkAdd(cy,cx-1,'L')
    
    if test==(-1,-1):
        # turn right/up or up/left:
        checkAdd(cy+1,cx,'L')
        checkAdd(cy+1,cx-1,'L')
        checkAdd(cy,cx-1,'L')
        checkAdd(cy-1,cx,'R')
        checkAdd(cy-1,cx+1,'R')
        checkAdd(cy,cx+1,'R')
        
    if test==(1,-1):
        # turn left/down or down/right:
        checkAdd(cy-1,cx,'R')
        checkAdd(cy-1,cx-1,'R')
        checkAdd(cy,cx-1,'R')
        checkAdd(cy+1,cx,'L')
        checkAdd(cy+1,cx+1,'L')
        checkAdd(cy,cx+1,'L')
    if test==(1,1):
        # turn right/down or down/left
        checkAdd(cy-1,cx,'L')
        checkAdd(cy-1,cx+1,'L')
        checkAdd(cy,cx+1,'L')
        checkAdd(cy+1,cx,'R')
        checkAdd(cy+1,cx-1,'R')
        checkAdd(cy,cx-1,'R')       


# flood the rest of the grid with L/R info:
for _ in range(10):
    for (y,x) in list(inout.keys()):
        if inout[(y,x)]=='L':
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    checkAdd(y+dy,x+dx,'L')
        if inout[(y,x)]=='R':
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    checkAdd(y+dy,x+dx,'R') 

# assume 'interior' is the smaller count of the L/R counts?
# at least in my input, there is significant "outside" space on the border of the grid
# probably some more principled way to do this though...

lCt = len([x for x in inout if inout[x]=='L'])
rCt = len([x for x in inout if inout[x]=='R'])
B = min(lCt,rCt)

print('Part A Solution:', A)
print('Part B Solution:', B)