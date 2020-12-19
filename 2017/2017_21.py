from utils import *
from copy import deepcopy
import numpy as np

inp = get_input(2017,21)

def to_hash(grd):
    return(tuple([grd[i][j] for i in range(len(grd)) for j in range(len(grd[0]))]))

# Group of symmetries is D4; generate 'em all!
def d4(sq):
    full = set()
    
    s = deepcopy(sq)
    
    for i in range(1,5):
        s = np.rot90(s)
        full.add(to_hash(s))
    s = s[::-1]
    for i in range(1,5):
        s = np.rot90(s)
        full.add(to_hash(s))
    return(full)

mapping = dict()

for x in inp:
    key, val = x.split(' => ')

    val = val.split('/')
    val = np.array([[t for t in x] for x in val],str)

    key = key.split('/')
    key = np.array([[t for t in x] for x in key],str)
    
    valid_keys = d4(key)
    for x in valid_keys:
        mapping[x] = val
        
        
def exp_grid(pat):
    new = deepcopy(pat)
    
    size = len(new)
    cols = []
    
    if size%2==0:
        for i in range(0,size,2):
            this_row = []
            for j in range(0,size,2):
                subgrid = new[i:i+2,j:j+2]
                key = to_hash(subgrid)
                this_row.append(mapping[key])
                
            cols.append(np.hstack(this_row))
      
    elif size%3==0:
        for i in range(0,size,3):
            this_row = []
            for j in range(0,size,3):
                subgrid = new[i:i+3,j:j+3]
                key = to_hash(subgrid)
                this_row.append(mapping[key])
                
            cols.append(np.hstack(this_row))
            
    return(np.vstack(cols))


init_pat = np.array([['.','#','.'],
                    ['.','.','#'],
                    ['#','#','#']])

s = deepcopy(init_pat)

for _ in range(18):
    s = exp_grid(s)
    if _ == 4:
        ans_A = to_hash(s).count('#')
    
ans_B = to_hash(s).count('#')


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)