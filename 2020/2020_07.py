from utils import *

## Part A answer is more or less what I did live. 
## Part B tooke me like 2 hours live. Sloppiness with how I was keeping track
## of multiplying throughout the process led to very large answers for awhile
## Then essentially rewrote from scratch in the dumbest way possible to get the right answer
## (writing down all chains from 'shiny gold' to a final bag and summing over each of these)
## The below is my attempt with a fresh mind the next day to doing something a little cleaner
## (without changing how I did the parsing/part A).
## Still pretty unclean, but better than the trash I wrote live.


## processing input
## adjacent is the adjacency list for the obvious graph
## should probably get faster with (e.g.) networkx

inp = get_input(2020,7)

inp2 = [x.split(' contain ') for x in inp]

adj = dd(list)

for x in inp2:
    key = x[0][:-5]
    for t in x[1].split(', '):
        adj[key].append([t.split(' ')[1]+' '+t.split(' ')[2],(t.split(' ')[0])])
for x in adj:
    for y in adj[x]:
        if y[1]=='no':
            y[1]=0
        else:
            y[1]=int(y[1]) 
    adj[x] = [tuple(y) for y in adj[x]]
    

##Part A

def is_shiny_gold(node):
    if node=='shiny gold':
        return False
    elif 'shiny gold' in [x[0] for x in adj[node]]:
        return True
    else:
        return any([is_shiny_gold(t[0]) for t in adj[node]])
    
ct_A=0
for n in list(adj.keys()):
    ct_A+=is_shiny_gold(n)


## Part B.
## Can't believe it's this short...

## supposed to be return # of bags nested in given bag
## including the bag itself


def total_bag_ct(node):
    bag_name = node[0]
    mult = node[1]
    return(mult*(1+sum([total_bag_ct(nodes) for nodes in adj[bag_name]])))

ct_B = total_bag_ct(('shiny gold', 1))-1



print('Part A Solution:', ct_A)
print('Part B Solution:', ct_B)
