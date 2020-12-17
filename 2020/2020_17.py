from utils import *
from copy import deepcopy as dc
from collections import defaultdict as dd


inp = get_input(2020,17)

# lol
# truly hideous
# seems like everyone was thrown by his 
# shifting indices in example
# spent a decent amount of time trying to debug against his examples

l_A = dd(str)
l_B = dd(str)

for i in range(len(inp)):
    for j in range(len(inp[0])):
        l_A[(0,i,j)]=inp[i][j]
        l_B[(0,i,j,0)]=inp[i][j]


def update_A(state):
    s = dc(state)
    t = dd(str)
    
    m_z = min([keys[0] for keys in s])
    M_z = max([keys[0] for keys in s])

    m_x = min([keys[1] for keys in s])
    M_x = max([keys[1] for keys in s])
    
    m_y = min([keys[2] for keys in s])
    M_y = max([keys[2] for keys in s])

    for z in range(m_z-1,M_z+2):
        for x in range(m_x-1,M_x+2):
            for y in range(m_y-1,M_y+2):
                on_ct = 0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        for dz in [-1,0,1]:
                            if (dz,dx,dy)!=(0,0,0):
                                 if s[(z+dz,x+dx,y+dy)]=='#':
                                        on_ct+=1

                if s[(z,x,y)]=='#':
                    if on_ct in [2,3]:
                        t[(z,x,y)]='#'
                elif s[(z,x,y)] in ['','.']:
                    if on_ct==3:
                        t[(z,x,y)]='#'
                else:
                    t[(z,x,y)]='.'
    return(t)



def update_B(state):
    s = dc(state)
    t = dd(str)
    
    m_z = min([keys[0] for keys in s])
    M_z = max([keys[0] for keys in s])

    m_x = min([keys[1] for keys in s])
    M_x = max([keys[1] for keys in s])
    
    m_y = min([keys[2] for keys in s])
    M_y = max([keys[2] for keys in s])
    
    m_w = min([keys[3] for keys in s])
    M_w = max([keys[3] for keys in s])    

    for z in range(m_z-1,M_z+2):
        for x in range(m_x-1,M_x+2):
            for y in range(m_y-1,M_y+2):
                for w in range(m_w-1,M_w+2):
                    on_ct = 0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                for dw in [-1,0,1]:
                                    if (dz,dx,dy,dw)!=(0,0,0,0):
                                         if s[(z+dz,x+dx,y+dy,w+dw)]=='#':
                                                on_ct+=1

                    if s[(z,x,y,w)]=='#':
                        if on_ct in [2,3]:
                            t[(z,x,y,w)]='#'
                    elif s[(z,x,y,w)] in ['','.']:
                        if on_ct==3:
                            t[(z,x,y,w)]='#'
                    else:
                        t[(z,x,y,w)]='.'
    return(t)





t_A = dc(l_A)
t_B = dc(l_B)
for _ in range(6):
    t_A = update_A(t_A)
    t_B = update_B(t_B)
    
ans_A = [t_A[key] for key in t_A].count('#')
ans_B = [t_B[key] for key in t_B].count('#')


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)