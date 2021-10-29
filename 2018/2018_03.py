from utils import *

inp = get_input(2018,3)

fab = dd(int)

for x in inp:
    num, drop_num = x.split('@ ')
    start, dims = drop_num.split(': ')
    startx, starty = [int(t) for t in start.split(',')]
    l,w = [int(t) for t in dims.split('x')]
    
    for i in range(l):
        for j in range(w):
            fab[(i+startx,j+starty)]+=1

A = 0
for pt in fab:
    if fab[pt]>1:
        A+=1
        
for x in inp:
    num, drop_num = x.split('@ ')
    start, dims = drop_num.split(': ')
    startx, starty = [int(t) for t in start.split(',')]
    l,w = [int(t) for t in dims.split('x')]
    
    check = 0
    for i in range(l):
        for j in range(w):
            if fab[(i+startx,j+starty)]>1:
                check=1
                break
    if check==0:
        B=int(num[1:])
        break
        


print('Part A Solution:', A)
print('Part B Solution:', B)