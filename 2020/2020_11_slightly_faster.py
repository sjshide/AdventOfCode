from utils import *

from collections import defaultdict as dd

inp = get_input(2020,11)

initial_state = dd(str)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        initial_state[(i,j)]=inp[i][j]
        
seen_1 = dd(list)
seen_2 = dd(list)
seen_by_1 = dd(list)
seen_by_2 = dd(list)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] in 'L#':
            for idif in [-1,0,1]:
                for jdif in [-1,0,1]:
                    if (idif,jdif)!=(0,0):
                        if i+idif in range(len(inp)) and j+jdif in range(len(inp[0])):
                            seen_1[(i,j)].append((i+idif,j+jdif))
                            seen_by_1[(i+idif,j+jdif)].append((i,j))


            for idif in [-1,0,1]:
                for jdif in [-1,0,1]:
                    I,J =i,j
                    if (idif,jdif)!=(0,0):
                        while True:
                            I+=idif
                            J+=jdif
                            if not (I in range(len(inp)) and J in range(len(inp[0]))):
                                break
                            if inp[I][J] in 'L#':
                                seen_2[(i,j)].append((I,J))
                                seen_by_2[(I,J)].append((i,j))
                                break

def update_1(m, to_check):
    local = dd(str)
    new_to_check=set()
    for inds in to_check:
        seen = [m[seen_inds] for seen_inds in seen_1[inds]]
        seen_filled = seen.count('#')

        if m[inds]=='L':
            if seen_filled==0:
                local[inds] = '#'
                new_to_check.update(seen_by_1[inds])
        elif m[inds]=='#':
            if seen_filled>=4:
                local[inds]= 'L'
                new_to_check.update(seen_by_1[inds])
    for inds in m:
        if not local[inds]:
            local[inds]=m[inds]
    return(local,new_to_check) 
                   
                   
def update_2(m, to_check):
    local = dd(str)
    new_to_check=set()
    for inds in to_check:
        seen = [m[seen_inds] for seen_inds in seen_2[inds]]
        seen_filled = seen.count('#')

        if m[inds]=='L':
            if seen_filled==0:
                local[inds] = '#'
                new_to_check.update(seen_by_2[inds])
        elif m[inds]=='#':
            if seen_filled>=5:
                local[inds]= 'L'
                new_to_check.update(seen_by_2[inds])
    for inds in m:
        if not local[inds]:
            local[inds]=m[inds]
    return(local,new_to_check)  

def part_A(state):
    s = state.copy()
    to_check = list(s.keys())
    
    while True:
        if not to_check:
            return([s[inds] for inds in s].count('#'))
        else:
            s,to_check = update_1(s,to_check)

                   
def part_B(state):
    s = state.copy()
    to_check = list(s.keys())
    
    while True:
        if not to_check:
            return([s[inds] for inds in s].count('#'))
        else:
            s,to_check = update_2(s,to_check) 

            
print('Part A Solution2:', part_A(initial_state))
print('Part B Solution2:', part_B(initial_state))