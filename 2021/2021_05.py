from utils import *

# 36/109. Wrong bounds on B cost me the double global

inp = get_input(2021,5)

pts_A = dd(int)
pts_B = dd(int)


for t in inp:
    first, second = t.split(' -> ')
    
    fx, fy = [int(x) for x in first.split(',')]
    sx, sy = [int(x) for x in second.split(',')]
    
    if fx==sx:
        for i in range(min(fy,sy),max(fy,sy)+1):
            pts_A[(fx,i)]+=1
            pts_B[(fx,i)]+=1
    elif fy==sy:
        for i in range(min(fx,sx),max(fx,sx)+1):
            pts_A[(i,fy)]+=1  
            pts_B[(i,fy)]+=1
                 
    else:
        if fx<sx:
            xstep=1
        else:
            xstep=-1
        if fy<sy:
            ystep=1
        else:
            ystep=-1
        for i in range(abs(fx-sx)+1):
            pts_B[(fx+xstep*i,fy+ystep*i)]+=1


A = 0
B = 0
for pt in pts_A:
    if pts_A[pt]>1:
        A+=1
for pt in pts_B:
    if pts_B[pt]>1:
        B+=1
            

print('Part A Solution:', A)
print('Part B Solution:', B)