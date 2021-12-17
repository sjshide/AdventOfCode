from utils import *

inp = get_input(2021,17)

t = inp.split(' ')
xmin, xmax = [int(l) for l in t[2][2:-1].split('..')]
ymin, ymax = [int(l) for l in t[3][2:].split('..')]

def step(x, y, vx, vy):
    x+=vx
    y+=vy
    vx = max(vx-1,0)
    vy-=1
    
    return(x,y,vx,vy)


def is_good(vx,vy):    
    x, y = 0,0    
    highest = -1    
    while x<xmax and y>ymin:
        x,y,vx,vy = step(x,y,vx,vy)
        
        if y>highest:
            highest=y
            
        if xmin<=x<=xmax and ymin<=y<=ymax:
            return((highest,1))
        
    return((0,0))


# live, did 0-1000 for vx, -1000-1000 for vy
# note that y is always eventually 0 if vy starts >0, with next step -vy, so just need to check in ymin,-ymin
# if vx>xmax, totally misses the box, so just need to check to xmax
# will add some +3s to be safe

As=[]
Bs=[]
for vx in range(xmax+3):
    for vy in range(ymin-3,-ymin+3):
        a,b = is_good(vx,vy)
        As.append(a)
        Bs.append(b)


print('Part A Solution:', max(As))
print('Part B Solution:', sum(Bs))
