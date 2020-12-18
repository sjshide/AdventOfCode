from utils import *

inp = get_input(2017,7)

pointers = set()
pointees = set()

weights = dict()
children = dd(list)
parent = dd(list)

for x in inp:
    m = x.split('->')

    this_node = m[0].split(' ')[0]
    
    pointers.add(this_node)
    weights[this_node] = int(m[0].split(' ')[1][1:-1])
    
    if '->' in x:
        for t in m[1][1:].split(', '):
            pointees.add(t)
            
            children[this_node].append(t)
            parent[t].append(this_node)
            
def tow_sum(node,total=0):
    if children[node]==[]:
        return (total+weights[node])
    else:
        return(total + weights[node]+sum([tow_sum(x,total) for x in children[node]]))
    

node = list(pointers-pointees)[0]    
while True:
    next_layer = [(x,tow_sum(x)) for x in children[node]]
    vals = dd(int)
    
    for x in next_layer:
        vals[x[1]]+=1
    if len(vals)==1:
        ans_B = weights[node]-dif
        break
    else:
        for t in vals:
            if vals[t]==1:
                next_off = t
            else:
                corr = t
        dif = next_off-corr
        node = [x[0] for x in next_layer if x[1]==next_off][0]


print('Part A Solution:',list(pointers-pointees)[0])
print('Part B Solution:', ans_B)