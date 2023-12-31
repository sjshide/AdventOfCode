from utils import *

inp = get_input(2023,23)

g = grid2dict(inp)
GA = nx.DiGraph()
GB = nx.DiGraph()
for (y,x) in g:
    if g[(y,x)] in '.><v^':
        GA.add_node((y,x))
        GB.add_node((y,x))
for (y,x) in GA.nodes():
    if g[(y,x)]=='^':
        GA.add_edge((y,x),(y-1,x))
    elif g[(y,x)]=='v':
        GA.add_edge((y,x),(y+1,x))
    elif g[(y,x)]=='<':
        GA.add_edge((y,x),(y,x-1))
    elif g[(y,x)]=='>':
        GA.add_edge((y,x),(y,x+1))
    else:
        if (y-1,x) in GA.nodes():
            GA.add_edge((y,x),(y-1,x))
        if (y+1,x) in GA.nodes():
            GA.add_edge((y,x),(y+1,x))
        if (y,x-1) in GA.nodes():
            GA.add_edge((y,x),(y,x-1))
        if (y,x+1) in GA.nodes():
            GA.add_edge((y,x),(y,x+1))
        
    if (y-1,x) in GB.nodes():
        GB.add_edge((y,x),(y-1,x))
    if (y+1,x) in GB.nodes():
        GB.add_edge((y,x),(y+1,x))
    if (y,x-1) in GB.nodes():
        GB.add_edge((y,x),(y,x-1))
    if (y,x+1) in GB.nodes():
        GB.add_edge((y,x),(y,x+1))
        
start = [(y,x) for (y,x) in GA.nodes() if y==0][0]
end = [(y,x) for (y,x) in GA.nodes() if y==len(inp)-1][0]

subG = nx.Graph()
for x in GB.nodes():
    if len(list(GB.neighbors(x)))>2:
        subG.add_node(x)
subG.add_node(start)
subG.add_node(end)

for (y,x) in subG.nodes():
    for nb in list(GB.neighbors((y,x))):
        last = (y,x)
        ct=1
        curr = dc(nb)
        while curr not in subG.nodes():
            newnb = [n for n in GB.neighbors(curr) if n!=last][0]
            ct+=1
            last=curr
            curr=newnb
        subG.add_edge((y,x),curr,weight=ct)

A = 0
for x in nx.all_simple_paths(GA,start,end):
    total = len(x)-1
    if total>A:
        A=total

B = 0
for x in nx.all_simple_paths(subG,start,end):
    total = 0
    for i in range(len(x)-1):
        total+=subG.edges[(x[i],x[i+1])]['weight']
    if total>B:
        B=total

print('Part A Solution:', A)
print('Part B Solution:', B)