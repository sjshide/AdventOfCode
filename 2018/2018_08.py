from utils import *

inp = [int(x) for x in get_input(2018,8).split(' ')]


count = 0
nodes = dd(list)
pars = dd(list)

# return (length of stuff processed this round, remaining unproc'd graph)
def parse_graph(l, parent):
    global count
    this_node = int(count)
    ll = l[2:]
    children, meta = l[:2]
    
    if not children:
        nodes[this_node] = ll[:meta]
        pars[this_node] = [parent]
        
        return(2+meta, l[2+meta:])
    
    else:
        indct=0
        for _ in range(children):
            count+=1
            this_ct, ll = parse_graph(ll,this_node)
            indct+=this_ct
            
        nodes[this_node]=ll[:meta]
        pars[this_node]=[parent]

        return(2+meta+indct,ll[meta:])
    
parse_graph(inp,-1)

#A
A=0
for x in nodes:
    A+=sum(nodes[x])

    
#B
ch = dd(list)

for x in pars:
    ch[pars[x][0]].append(x)
    
def get_score(node):
    if not ch[node]:
        return sum(nodes[node])
    
    else:
        this_score = 0
        for x in nodes[node]:
            try:
                this_score+=get_score(ch[node][x-1])
            except:
                this_score+=0
        return(this_score)

    
B = get_score(0)    
    

print('Part A Solution:', A)
print('Part B Solution:', B)