from utils import *
from copy import deepcopy as dc

inp = get_input(2020,24)

## lulled into using complex numbers originally due to a 2017 problem that required them
## ended up searching other (integral!) rep's of a hex grid after screwing around with rounding errors for a while
## cf https://www.redblobgames.com/grids/hexagons/


def parse_dirs(d):
    dirs = []
    i=0
    while i <len(d):
        if d[i] in 'sn':
            dirs.append(d[i:i+2])
            i+=2
        else:
            dirs.append(d[i])
            i+=1
    return(dirs)

# grid representation
deltas = {
    'e': (1,-1,0),
    'ne': (1,0,-1),
    'nw': (0,1,-1),
    'w': (-1,1,0),
    'sw': (-1,0,1),
    'se': (0,-1,1)
}

def get_xyz(l):
    pos = (0,0,0)
    for inst in l:
        dx,dy,dz = deltas[inst]
        pos  = (pos[0]+dx,pos[1]+dy,pos[2]+dz)        
    return(pos)

def blksum(tz):
    total = 0
    for x in tz:
        total+=tz[x]
    return(total)

tiles = dd(bool)
for d in inp:
    key = get_xyz(parse_dirs(d))
    tiles[key] = not tiles[key]
    
ans_A = blksum(tiles)

def day_flip(t):
    tz = dc(t)
    to_check = set()
    to_flip = set()
    
    for base in tz:
        if tz[base]:
            to_check.add(base)
            for delt in deltas:
                dx,dy,dz = deltas[delt]
                to_check.add((base[0]+dx,base[1]+dy,base[2]+dz))
    
    for base in to_check:
        blkct=0
        for delt in deltas:
            dx,dy,dz = deltas[delt]
            blkct+=tz[(base[0]+dx,base[1]+dy,base[2]+dz)]
        
        if tz[base]:
            if blkct==0 or blkct>2:
                to_flip.add(base)
        else:
            if blkct==2:
                to_flip.add(base)
                
    for base in to_flip:
        tz[base]=not tz[base]
     
    return(tz) 

this = dc(tiles)
for _ in range(100):
    this = day_flip(this)

ans_B = blksum(this)


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)