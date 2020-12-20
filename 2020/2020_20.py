from utils import *
import numpy as np
from copy import deepcopy as dc

inp = get_input(2020,20)


# key:value = (tile id): (grid in list form)
tiles = dd(list)
this = []
for x in inp:
    if 'Tile' in x:
        key = x.split(' ')[1][:-1]
    
    elif not x:
        tiles[key]=dc(this)
        this=[]
    else:
        this.append(list(x))
tiles[key] = dc(this)


# key:value = (tile id): (all sides in all orientations of tile)
tile_sides= dd(set)
for x in tiles:
    g = tiles[x]
    s1 = tuple(g[0])
    s2 = tuple(g[len(g)-1])
    s3 = tuple([g[i][0] for i in range(len(g))])
    s4 = tuple([g[i][len(g[0])-1] for i in range(len(g))])

    for s in [s1,s2,s3,s4]:
        tile_sides[x].add(tuple(s))
        tile_sides[x].add(tuple(s[::-1]))


# key:value = (side):(which tiles that side appears in)
side_dict = dd(list)
for x in tile_sides:
    for side in tile_sides[x]:
        side_dict[side].append(x)
      
    
# A
ans_A = 1
for x in tile_sides:
    this = []
    for side in tile_sides[x]:
        this.append(len(side_dict[side]))
    if this.count(1)>2: #more than 1 side that only matches this tile
        ans_A*=(int(x))
        

# B
# Now to actually do the work....
# General strategy is fix a tile in upper left corner
# Then build out first row and first column from this
# then fill in the rest
# first just with correct ids, then with actual rotated tiles


# key:value is (tile id):(tiles that share a side with key)
nbs = dd(set)
for x in tile_sides:
    for side in tile_sides[x]:
        nbs[x].update(side_dict[side])
        nbs[x].remove(x)

def get_sides(g):
    s1 = tuple(g[0])
    s2 = tuple(g[len(g)-1])
    s3 = tuple([g[i][0] for i in range(len(g))])
    s4 = tuple([g[i][len(g[0])-1] for i in range(len(g))])
    
    return(s1,s2,s3,s4)


# slightly lucky in that the first corner tile I looked at was oriented correctly
# to be the upper-left hand corner of grid.
# Hard coding for now, but will think about how to do this in general...

# tile id by locations in the larger grid
last = '2521'
locs = [['' for _ in range(12)] for _ in range(12)]
seen = set()
seen.add(last)
top,bot,left,right = get_sides(tiles[last])

right_tile = [t for t in side_dict[right] if t!=last][0]
down_tile = [t for t in side_dict[bot] if t!=last][0]

locs[0][0] = last
locs[0][1] = right_tile
locs[1][0] = down_tile

last = down_tile
for i in range(2,12):
    seen.add(last)
    
    t = nbs[last]
    
    for x in t:
        if (x not in seen) and (len(nbs[x])<4):
            break
    last=x
    locs[i][0]=last

last = right_tile
for i in range(2,12):
    seen.add(last)
    
    t = nbs[last]
    
    for x in t:
        if (x not in seen) and (len(nbs[x])<4):
            break
    last=x
    locs[0][i]=last

for i in range(1,12):
    for j in range(1,12):
        up = locs[i-1][j]
        left= locs[i][j-1]
        
        for x in nbs:
            if x not in seen and up in nbs[x] and left in nbs[x]:
                break
        locs[i][j]=x
        seen.add(x)
        

        
## Now that we know which tile lives where, rotate them to match them up
## following the same pattern through the grid as before

## key:value = (tile id):(tile correctly rotated to match neighbors)
rot_tiles = dict()

# here's where I'm using the fact that 2521 was correctly oriented to be the 
# upper left corner of my grid with no rotations/flips
rot_tiles['2521'] = np.array(dc(tiles['2521']))

# run through all rotations/flips of a tile, writing down when it matches the 
# neighbor either up/to the left/ both (where appropriate)
# should be 1 such configuration for each tile

l = dc(locs)
# upper border
for i in range(1,12):
    this_id = l[i][0]
    last_id = l[i-1][0]
    
    bot = list(rot_tiles[last_id][9])

    x = np.array(dc(tiles[this_id]))
    
    match = []
    for _ in range(4):
        if list(x[0,:])==bot:
            match.append(x)
        x = np.rot90(x)

    x=np.flip(x,0)
    for _ in range(4):
        if list(x[0,:])==bot:
            match.append(x)
        x = np.rot90(x)
    for t in match:
        rot_tiles[this_id]=t

# left border
for i in range(1,12):
    this_id = l[0][i]
    last_id = l[0][i-1]
    
    right = list(rot_tiles[last_id][:,9])
    x = np.array(dc(tiles[this_id]))
    
    match = []
    for _ in range(4):
        if list(x[:,0])==right:
            match.append(x)
        x = np.rot90(x)

    x=np.flip(x,0)
    for _ in range(4):
        if list(x[:,0])==right:
            match.append(x)
        x = np.rot90(x)
    for t in match:
        rot_tiles[this_id]=t

        
# rest of the grid        
for i in range(1,12):
    for j in range(1,12):
        this_id = l[i][j]
        left_id = l[i][j-1]
        up_id = l[i-1][j]

        right = list(rot_tiles[left_id][:,9])
        bot = list(rot_tiles[up_id][9])        
        
        x = np.array(dc(tiles[this_id]))

        match = []
        for _ in range(4):
            if list(x[:,0])==right and list(x[0,:])==bot:
                match.append(x)
            x = np.rot90(x)

        x=np.flip(x,0)
        for _ in range(4):
            if list(x[:,0])==right and list(x[0,:])==bot:
                match.append(x)
            x = np.rot90(x)
        for t in match:
            rot_tiles[this_id]=t        

            
## Actually form the picture
## run through, chopping off border, and using hstack/vstack
rows = []
for i in range(12):
    cols = []
    for j in range(12):
        this_id = l[i][j]
        grid = dc(rot_tiles[this_id])
        cols.append(grid[1:-1,1:-1])
    
    cols = np.hstack(cols)
    rows.append(cols)
picture = np.vstack(rows)


monster = ['                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   ']

# get indices of a monster in all orientations
no_flip = set()
for i in range(len(monster)):
    for j in range(len(monster[0])):
        if monster[i][j]=='#':
            no_flip.add((i,j))

h_flip = set()
v_flip = set()
both_flip = set()
for (i,j) in no_flip:
    h_flip.add((i,19-j))
    v_flip.add((2-i,j))
    both_flip.add((2-i,19-j))

no_rot = set([(j,i) for (i,j) in no_flip])
h_rot = set([(j,i) for (i,j) in h_flip])
v_rot =set([(j,i) for (i,j) in v_flip])
both_rot = set([(j,i) for (i,j) in both_flip])


# m_check[i,j]=1 if picture[i,j] is in a monster, 0 otherwise
m_check = np.zeros((98,98))

for i in range(96-3):
    for j in range(96-20):
        for shape in [no_flip,h_flip,v_flip,both_flip]:
            inds_to_check = []
            for (ip,jp) in shape:
                inds_to_check.append((i+ip,j+jp))
            
            ismons = [picture[ip,jp] for (ip,jp) in inds_to_check]
            if ismons.count('#')==len(ismons):
                for (ip,jp) in inds_to_check:
                    m_check[ip,jp]=1
            
for i in range(96-20):
    for j in range(96-3):
        for shape in [no_rot,h_rot,v_rot,both_rot]:
            inds_to_check = []
            for (ip,jp) in shape:
                inds_to_check.append((i+ip,j+jp))
            
            ismons = [picture[ip,jp] for (ip,jp) in inds_to_check]
            if ismons.count('#')==len(ismons):
                for (ip,jp) in inds_to_check:
                    m_check[ip,jp]=1
                    
unique, counts = np.unique(picture, return_counts=True)
ct_d = dict(zip(unique, counts))

ans_B = int(ct_d['#'] - m_check.sum())

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)