from utils import *

inp = get_input(2017,22)

def step_A(grid, i, j, direc):
    new_inf = 0
    loc_grid=grid.copy()
    inf_check =0
    if loc_grid[(i,j)]=='#':
        direc*=(1j)
        loc_grid[(i,j)] = '.'
    else:
        direc*=(-1j)
        loc_grid[(i,j)]= '#'
        inf_check=1
    return (loc_grid,i+direc.imag,j+direc.real,direc,inf_check)        


def step_B(i, j, direc):
    new_inf = 0
    inf_check =0
    if grid[(i,j)] in '.':
        direc*=(-1j)
        grid[(i,j)]='W'
    elif grid[(i,j)]=='W':
        grid[(i,j)] = '#'
        inf_check=1
    elif grid[(i,j)]=='#':
        direc*=(1j)
        grid[(i,j)]='F'
    elif grid[(i,j)]=='F':
        direc*=(-1)
        grid[(i,j)]='.'

    return (i+direc.imag,j+direc.real,direc,inf_check)



state = dd(str)
m = len(inp)
for i in range(m):
    for j in range(m):
        state[(i-(m//2),j-(m//2))]=inp[i][j]

        
        
# A       
grid=state.copy()
i=0
j=0
direct = -1j
ans_A = 0
for _ in range(10_000):    
    grid,i,j,direct,ct = step_A(grid,i,j,direct)
    ans_A+=ct


# B
grid = state.copy()
i=0
j=0
direct = -1j
ans_B = 0
for _ in range(10_000_000):    
    i,j,direct,ct = step_B(i,j,direct)    
    ans_B+=ct


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)