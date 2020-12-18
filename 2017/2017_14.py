from utils import *

inp = get_input(2017,14)

d = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def knot(steps = [], length=256, init=list(range(256)), current_pos=0, skip=0):
    for step in steps:
        if current_pos+step<length:
            ind = current_pos
            ind2 = current_pos+step
            init = init[:ind]+(init[ind:ind2])[::-1]+init[ind2:]
            
        else:
            ind=current_pos
            ind2 = (current_pos+step)%length
            local = init[ind:]+init[:ind2]
            local = local[::-1]
            init = local[length-ind:]+init[ind2:ind]+local[:length-ind]

        current_pos = (current_pos+step+skip)%length
        skip+=1
        
    return(init, current_pos, skip)


def ascii_to_hex(s):
    m = hex(s)[2:]
    if len(m) == 1:
        m = '0'+m
    return(m)

def str_to_hash(s):
    steps=[ord(i) for i in s]+[17, 31, 73, 47, 23]
    init = list(range(256))
    current_pos = 0
    skip = 0
    
    for _ in range(64):
        init, current_pos, skip = knot(steps, 256, init, current_pos, skip)
        
    dense = []
    for i in range(16):
        dense_val = 0
        for m in init[16*i:16*(i+1)]:
            dense_val = dense_val^m
        dense.append(dense_val)
        
    final_hash = ''
    for x in dense:
        final_hash+=ascii_to_hex(x)
    return(final_hash)


def hex_to_bin(h):
    ans = ''
    for i in h:
        ans+=d[i]
    return(ans)  


rows = [hex_to_bin(str_to_hash(inp+'-'+str(i))) for i in range(128)]

ans_A = sum([sum([int(i) for i in x]) for x in rows])

def get_nbs(rows):
    graph_nbs = dict()
    
    for i in range(128):
        for j in range(128):
            if rows[i][j]=='1':
                graph_nbs[(i,j)] = []
    
    for m in graph_nbs:
        i,j = m
        if (i+1,j) in graph_nbs:
            graph_nbs[m].append((i+1,j))
        if (i-1,j) in graph_nbs:
            graph_nbs[m].append((i-1,j))
        if (i,j+1) in graph_nbs:
            graph_nbs[m].append((i,j+1))
        if (i,j-1) in graph_nbs:
            graph_nbs[m].append((i,j-1))
    return(graph_nbs)

nbs = get_nbs(rows)

def cc(node,seen = set()):
    seen.add(node)
    for x in nbs[node]:
        if x not in seen:
            new_nbs = cc(x,seen)
    return(seen)


ans_B=0
s = list(nbs)
while s:
    this = s[0]
    a = cc(this,set())
    for x in a:
        s.remove(x)
    ans_B+=1




print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)