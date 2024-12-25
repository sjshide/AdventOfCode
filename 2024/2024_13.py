from utils import *

inp = get_input(2024,13)

# was actually kind of annoyed that there were no answers with det=0
# can just do some linear algebra

A = 0
B = 0

for i in range(0,len(inp),4):
    thisGame = inp[i:i+4]
    
    a = thisGame[0]
    v1 = a.split(': ')[1]
    v2 = v1.split(', ')
    ax,ay = [int(v.split('+')[1]) for v in v2]
    
    b = thisGame[1]
    v1 = b.split(': ')[1]
    v2 = v1.split(', ')
    bx,by = [int(v.split('+')[1]) for v in v2]
 
    p = thisGame[2]
    v1 = p.split(': ')[1]
    v2 = v1.split(', ')
    px,py = [int(v.split('=')[1]) for v in v2] 

    det = ax*by-ay*bx
    sA = by*px-bx*py
    tA = ax*py-ay*px
    if not sA%det:
        if not tA%det:
            s = sA//det
            t = tA//det
            A+=3*s+t
    sB = by*(10000000000000+px)-bx*(10000000000000+py)
    tB = ax*(10000000000000+py)-ay*(10000000000000+px)
    if not sB%det:
        if not tB%det:
            s = sB//det
            t = tB//det
            B+=3*s+t
    
print('Part A Solution:', A)
print('Part B Solution:', B)