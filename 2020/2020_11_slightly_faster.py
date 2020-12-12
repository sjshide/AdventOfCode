from utils import *

from collections import defaultdict as dd

inp = get_input(2020,11)

initial_state = dd(str)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] in 'L#':
            initial_state[(i,j)]=inp[i][j]
        
seen_A = dd(list)
seen_B = dd(list)
seen_by_A = dd(list)
seen_by_B = dd(list)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] in 'L#':
            for idif in [-1,0,1]:
                for jdif in [-1,0,1]:
                    if (idif,jdif)!=(0,0):
                        
                        # seen, seen_by for part 1
                        if i+idif in range(len(inp)) and j+jdif in range(len(inp[0])) and inp[i+idif][j+jdif] in 'L#':
                            seen_A[(i,j)].append((i+idif,j+jdif))
                            seen_by_A[(i+idif,j+jdif)].append((i,j))
                        
                        # seen, seen_by for part 2
                        I,J =i,j
                        while True:
                            I+=idif
                            J+=jdif
                            if not (I in range(len(inp)) and J in range(len(inp[0]))):
                                break
                            if inp[I][J] in 'L#':
                                seen_B[(i,j)].append((I,J))
                                seen_by_B[(I,J)].append((i,j))
                                break

part_dict = {'A':(seen_A, seen_by_A, 4),'B':(seen_B, seen_by_B, 5)}

def update(m, to_check, part):
    seen, seen_by, thresh = part_dict[part]
    local = dd(str)
    new_to_check=set()
    
    for inds in to_check:
        seen_chairs = [m[seen_inds] for seen_inds in seen[inds]]
        seen_filled = seen_chairs.count('#')
        if m[inds]=='L':
            if seen_filled==0:
                local[inds] = '#'
                new_to_check.update(seen_by[inds])
        elif m[inds]=='#':
            if seen_filled>=thresh:
                local[inds]= 'L'
                new_to_check.update(seen_by[inds])
    for inds in m:
        if not local[inds]:
            local[inds]=m[inds]
    return(local,new_to_check) 
                   

def run_part(part, state):
    s = state.copy()
    to_check = list(s.keys())
    while True:
        if not to_check:
            return([s[inds] for inds in s].count('#'))
        else:
            s,to_check = update(s,to_check,part)
            
print('Part A Solution:', run_part('A', initial_state))
print('Part B Solution:', run_part('B', initial_state))
