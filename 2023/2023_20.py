from utils import *

# Not the prettiest write-up...

inp = get_input(2023,20)

# A
# Will reconstruct the graph for B
G = nx.DiGraph()
conjs = []
flips = []
nodeType = dict()
for x in inp:
    src, trgts = x.split(' -> ')
    
    if src[0]=='%': #flip-flop
        # 0 off, 1 on
        G.add_node(src[1:],stat=0)
        flips.append(src[1:])
        nodeType[src[1:]]='FLIP'
    elif src[0]=='&':
        G.add_node(src[1:],conj=dict())
        conjs.append(src[1:])
        nodeType[src[1:]]='CONJ'
    else: # broadcast
        G.add_node(src)
        
for x in inp:
    src, trgts = x.split(' -> ')
    
    if src[0] in '%&':
        src=src[1:]
    for y in trgts.replace(',',' ').split():
        G.add_edge(src,y)
        if y in conjs:
            G.nodes[y]['conj'][src]=0
    
G.add_node('button')
G.add_edge('button','broadcaster')

cts = [0,0] #low, high
for _ in range(1000):
    activePulses = [(0,'button','button')]
    while activePulses:
        thisPulse = activePulses.pop(0)
        pulse, node, src = thisPulse

        if node!='button':
            cts[pulse]+=1

        if node in ['button','broadcaster']:
            for y in G.neighbors(node):
                activePulses.append((pulse,y,node))

        elif node in flips:
            if pulse==0:
                newPulse = (G.nodes[node]['stat']+1)%2
                G.nodes[node]['stat']=newPulse
                for y in G.neighbors(node):
                    activePulses.append((newPulse,y,node))
                    
        elif node in conjs:
            G.nodes[node]['conj'][src]=pulse
            if set(G.nodes[node]['conj'].values()) == set([1]):
                newPulse = 0
            else:
                newPulse = 1
            for y in G.neighbors(node):
                activePulses.append((newPulse,y,node))    
                

# B
# For me, 'qn' was the conjunction sending a signal to rx
# Need all neighbors to be high.
# Could programmatically figure this out I guess, but 
# this one for sure requires examining inputs anyways...
# 'qn' had 4 neighbors, with cycle length = to first time hit
# and all were prime
# I'll use that in this although I checked more throroughly live
# Recreate graph:
G = nx.DiGraph()
conjs = []
flips = []
nodeType = dict()
for x in inp:
    src, trgts = x.split(' -> ')
    
    if src[0]=='%': #flip-flop
        # 0 off, 1 on
        G.add_node(src[1:],stat=0)
        flips.append(src[1:])
        nodeType[src[1:]]='FLIP'
    elif src[0]=='&':
        G.add_node(src[1:],conj=dict())
        conjs.append(src[1:])
        nodeType[src[1:]]='CONJ'
    else: # broadcast
        G.add_node(src)
G.add_node('button')
G.add_edge('button','broadcaster')
for x in inp:
    src, trgts = x.split(' -> ')
    
    if src[0] in '%&':
        src=src[1:]
    for y in trgts.replace(',',' ').split():
        G.add_edge(src,y)
        if y in conjs:
            G.nodes[y]['conj'][src]=0
# check until we've seen each neighbor of qn receive a high pulse.            
toCheck = set(G.nodes['qn']['conj'].keys())
i = 1
ixs = []
while toCheck:
    activePulses = [(0,'button','button')]
    while activePulses:
        thisPulse = activePulses.pop(0)
        pulse, node, src = thisPulse

        if node!='button':
            cts[pulse]+=1

        if node in ['button','broadcaster']:
            for y in G.neighbors(node):
                activePulses.append((pulse,y,node))

        elif node in flips:
            if pulse==0:
                newPulse = (G.nodes[node]['stat']+1)%2
                G.nodes[node]['stat']=newPulse
                for y in G.neighbors(node):
                    activePulses.append((newPulse,y,node))
                    
        elif node in conjs:
            G.nodes[node]['conj'][src]=pulse
            if set(G.nodes[node]['conj'].values()) == set([1]):
                newPulse = 0
            else:
                newPulse = 1
            for y in G.neighbors(node):
                activePulses.append((newPulse,y,node))     
        
        for nb in toCheck:
            toRemove = set()
            if G.nodes['qn']['conj'][nb]==1:
                toRemove.add(nb)
                ixs.append(i)
            toCheck = toCheck - toRemove
    i+=1
# Take the product
B = 1
for x in ixs:
    B*=x

print('Part A Solution:', cts[0]*cts[1])
print('Part B Solution:', B)