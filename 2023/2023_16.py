from utils import *

inp = get_input(2023,16)

# Make a digraph and walk around it
# Not much else to it...

g = grid2dict(inp)
G = nx.DiGraph()
for (y,x) in g:
    for direc in 'UDLR':
        G.add_node(tuple((y,x,direc)))
                
for (y,x) in g:
    if g[(y,x)]=='.':
        if y>0:
            G.add_edge((y,x,'U'),(y-1, x, 'U'))
        if x>0:
            G.add_edge((y,x,'L'),(y, x-1, 'L'))
        if y<len(inp)-1:
            G.add_edge((y,x,'D'),(y+1, x, 'D'))
        if x<len(inp[0])-1:
            G.add_edge((y,x,'R'),(y, x+1, 'R'))
    
    elif g[(y,x)]=='\\':
        if x>0:
            G.add_edge((y,x,'U'),(y, x-1, 'L'))
        if y>0:
            G.add_edge((y,x,'L'),(y-1, x, 'U'))
        if x<len(inp[0])-1:
            G.add_edge((y,x,'D'),(y, x+1, 'R'))
        if y<len(inp)-1:
            G.add_edge((y,x,'R'),(y+1, x, 'D'))        
    
    elif g[(y,x)]=='/':
        if x<len(inp[0])-1:
            G.add_edge((y,x,'U'),(y, x+1, 'R'))
        if y<len(inp)-1:
            G.add_edge((y,x,'L'),(y+1, x, 'D'))
        if x>0:
            G.add_edge((y,x,'D'),(y, x-1, 'L'))
        if y>0:
            G.add_edge((y,x,'R'),(y-1, x, 'U'))   
            
    elif g[(y,x)]=='|':
        if y>0:
            G.add_edge((y,x,'U'),(y-1, x, 'U'))
            G.add_edge((y,x,'L'),(y-1, x, 'U'))
            G.add_edge((y,x,'R'),(y-1, x, 'U'))
        if y<len(inp)-1:
            G.add_edge((y,x,'D'),(y+1, x, 'D'))
            G.add_edge((y,x,'L'),(y+1, x, 'D'))
            G.add_edge((y,x,'R'),(y+1, x, 'D'))
            
    elif g[(y,x)]=='-':
        if x>0:
            G.add_edge((y,x,'L'),(y, x-1, 'L'))
            G.add_edge((y,x,'U'),(y, x-1, 'L'))
            G.add_edge((y,x,'D'),(y, x-1, 'L'))
        if x<len(inp[0])-1:
            G.add_edge((y,x,'R'),(y, x+1, 'R'))   
            G.add_edge((y,x,'U'),(y, x+1, 'R'))
            G.add_edge((y,x,'D'),(y, x+1, 'R'))

            
def getEnergized(start):
    currNodes = set()
    currNodes.add(start)
    visitedNodes = set()
    visitedNodes.add(start)
    while True:
        nextNodes = set()
        newCheck=0
        for node in currNodes:
            nbs = G.neighbors(node)
            for nb in nbs:
                if nb not in visitedNodes:
                    newCheck=1
                    visitedNodes.add(nb)
                    nextNodes.add(nb)
        if not newCheck:
            break
        currNodes = nextNodes
    
    return len(set([x[0:2] for x in visitedNodes]))

# Assume square grid (?)
l = len(inp)
B = 0
for ind in range(l):
    B = max(B, getEnergized((ind,0,'R')))
    B = max(B, getEnergized((ind,l-1,'L')))
    B = max(B, getEnergized((0,ind,'D')))
    B = max(B, getEnergized((l-1,ind,'U')))

print('Part A Solution:', getEnergized((0,0,'R')))
print('Part B Solution:', B)