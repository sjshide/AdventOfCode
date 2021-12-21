from utils import *

# one-observation wonder. 
# crux was noticing that algo[0]='#', algo[-1]='.'


inp = get_input(2021,20)

algo = inp[0]
image = grid2dict(inp[2:],dd(lambda:'.'))

def hashct(grid):
    ct = 0
    for key in grid:
        if grid[key]=='#':
            ct+=1
    return(ct)


def step(grid, parity):
    if parity:
        new_grid = dd(lambda:'#')
    else:
        new_grid = dd(lambda:'.')
         
    ys = [k[0] for k in grid]
    xs = [k[1] for k in grid]
    
    xmin,xmax = min(xs),max(xs)
    ymin,ymax = min(ys),max(ys)
    
    # making sure I padded enough...didn't want to think too hard about it
    for y in range(ymin-4,ymax+5):
        for x in range(xmin-4,xmax+5):
            s = ''
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if grid[(y+dy,x+dx)]=='#':
                        s+='1'
                    else:
                        s+='0'
            new_grid[(y,x)] = algo[int(s,2)]
            
    return(new_grid)


b = dc(image)
a = step(b,1)
b = step(a,0)

A = hashct(b)

for i in range(24):
    a=step(b,1)
    b=step(a,0)

B = hashct(b)


print('Part A Solution:', A)
print('Part B Solution:', B)