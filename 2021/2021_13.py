from utils import *

inp = get_input(2021,13)

locs = dict()
folds = []

for spot in inp:
    if ',' in spot:
        x,y = [int(t) for t in spot.split(',')]
        locs[(y,x)] = 1
        
    elif 'fold' in spot:
        coord = spot.split(' ')[-1]
        axis, val = coord.split('=')
        folds.append((axis,int(val)))
        
def do_fold(axis, val, spots):
    new_spots = dict()
    
    for spot in spots:
        if axis=='x':
            if spot[1]<val:
                new_spots[spot] =1
            else:
                new_spots[(spot[0],2*val-spot[1])]=1
        elif axis=='y':
            if spot[0]<val:
                new_spots[spot] =1
            else:
                new_spots[(2*val-spot[0],spot[1])]=1
                
    return(new_spots)

# A
A = len(do_fold(folds[0][0],folds[0][1],locs))

# B
new_locs = dc(locs)
for fold in folds:
    new_locs = do_fold(fold[0], fold[1], new_locs)
    
ys = [t[0] for t in new_locs.keys()]
xs = [t[1] for t in new_locs.keys()]


print('Part A Solution:', A)
print('Part B Solution:')
for i in range(min(ys),max(ys)+1):
    this_row = ''
    for j in range(min(xs),max(xs)+1):
        if (i,j) in new_locs:
            this_row+='[]'
        else:
            this_row+='  '
    print(this_row)
