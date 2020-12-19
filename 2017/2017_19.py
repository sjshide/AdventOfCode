from utils import *

inp = get_input(2017,19)

# get ending spot:
for i in range(1,len(inp)):
    for j in range(1,len(inp[0])):
        spc_ct = 0
        if inp[i][j]!=' ':
            if inp[i+1][j]==' ':
                spc_ct+=1
            if inp[i-1][j] == ' ':
                spc_ct+=1
            if inp[i][j+1]==' ':
                spc_ct+=1
            if inp[i][j-1]==' ':
                spc_ct+=1
            if spc_ct>2:
                final_i, final_j = i,j


ans_A = ''
ans_B = 0

direc = 'd' #u,d,l,r
d_step = dict()
d_step['d']=(1,0)
d_step['u']=(-1,0)
d_step['l']=(0,-1)
d_step['r']=(0,1)

y=0
x=inp[0].index('|')

while (y,x)!=(final_i,final_j):
    ans_B+=1
    
    this = inp[y][x]
    if this in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        ans_A+=this
    
    y_step, x_step = d_step[direc]
    
    if this=='+' and inp[y+y_step][x+x_step]==' ':
        loc_dir = 0
        if direc in ['u','d']:
            if inp[y][x-1]!=' ':
                loc_dir='l'
                x-=1
            else:
                loc_dir='r'
                x+=1
        if direc in ['r','l']:
            if inp[y+1][x]!=' ':
                loc_dir='d'
                y+=1
            else:
                loc_dir='u'
                y-=1
        direc = loc_dir
                
    else:
        y+=y_step
        x+=x_step

        
ans_A+=inp[7][65]    
ans_B+=1                

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)