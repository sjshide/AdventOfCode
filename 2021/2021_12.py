from utils import *
import networkx as nx

# networkx overkill here. 
# ended up just using the graph class then writing my own method
# could've just used an adjacency dict in retrospect

inp = get_input(2021,12)

G = nx.Graph()

for x in inp:
    s,f = x.split('-')
    G.add_edge(s,f)

#part: 1 (A) or 2 (B)
def small_check(path, part):
    d = dd(int)
    
    for x in path:
        d[x]+=1
    
    small = [spot for spot in d if spot.islower()]
    
    if d['start']<2 and d['end']<2:
        g2ct = 0
        for t in small:
            if d[t]>2:
                return(0)
            if d[t]>1:
                g2ct+=1
        if g2ct<part:
            return(1)
    return(0)


def solve_puzzle(part):
    paths = set([tuple(['start'])])
    overall = set()
    
    while True:
        new_paths = set()

        for path in paths:
            overall.add(path)
            last = path[-1]

            if last!='end':
                for nex in G.neighbors(last):
                    if small_check(list(path)+[nex],part):
                        new_paths.add(tuple(list(path)+[nex]))
        if paths==new_paths:
            break
        paths=new_paths

    soln = 0
    for x in overall:
        if x[0]=='start' and x[-1]=='end':
            soln+=1
    return(soln)
        

print('Part A Solution:', solve_puzzle(1))
print('Part B Solution:', solve_puzzle(2))