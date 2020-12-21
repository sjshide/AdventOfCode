from utils import *
import networkx as nx
from copy import deepcopy as dc

inp = get_input(2020,21)

ingreds = set()
allergens = set()
pairs = dict()

all2ing = dd(set)

for i in range(len(inp)):
    x = inp[i]
    ings, alls = x.split(' (contains ')
    ings = ings.split(' ')
    alls = alls[:-1]
    alls = alls.split(', ')
    
    pairs[i] = [ings,alls]
    ingreds.update(ings)
    allergens.update(alls)
    
for x in allergens:
    all2ing[x]=dc(ingreds)
    
for i in pairs:
    ings, alls = pairs[i]
    for this_all in alls:
        all2ing[this_all] = all2ing[this_all].intersection(set(ings))

possible = set()
for x in all2ing:
    possible = possible.union(all2ing[x])
    

ans_A = 0
for i in pairs:
    ings, alls= pairs[i]
    for y in ings:
        if y in ingreds-possible:
            ans_A+=1

# did by hand live. networkx for laughs here.
G = nx.Graph()
for x in all2ing:
    for y in all2ing[x]:
        G.add_edge(x,y)
match = nx.bipartite.maximum_matching(G)

ans_B = ''
for a in sorted(list(allergens)):
    ans_B+=(match[a]+',')
ans_B = ans_B[:-1]

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)