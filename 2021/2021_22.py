from utils import *

inp = get_input(2021,22)


# this took me ages...had thought inclusion/exclusion type argument,
# but took me a while to get an idea for implementing it,
# then had to debug...
# still don't have my head wrapped around exactly what's happening here...

def intersection(a,b):
    
    int_bds = []
    
    for i in range(3):
        mina,maxa,minb,maxb = a[2*i:2*i+2]+b[2*i:2*i+2]
        
        l = [mina,maxa,minb,maxb]
        
        # check for nontrivial intersection
        if mina==maxa and (mina<minb or mina>maxb):
            return(0)
        if minb==maxb and (minb<mina or minb>maxa):
            return(0)
        if len(set(l))==4 and (sorted(l) in [[mina,maxa,minb,maxb],
                                             [minb,maxb,mina,maxa]]):
            return(0)
        
        # if nontrivial, return the intersection
        int_bds+=sorted(l)[1:3]
    
    return(int_bds+[b[6],a[7]+1])

def area(pt):
    return((pt[1]-pt[0]+1)*(pt[3]-pt[2]+1)*(pt[5]-pt[4]+1))



def do_calc(l):
    newrs = []

    for r1 in l:
        loc = []
        if r1[-2]=='on':
            loc.append(r1)   
        for r2 in newrs:
            if intersection(r2,r1):
                loc.append(intersection(r2,r1))
        newrs+=loc
    
    ct = 0
    for x in newrs:
        ct+=(pow(-1,x[-1])*area(x))
    return(ct)



rects = []

# break out rectangles:
# xmin,xmax,ymin,ymax,zmin,zmax,on/off,depth

for pts in inp:
    turn, coords = pts.split(' ')
    
    x,y,z = coords.split(',')
    xr = [int(t) for t in x.split('=')[1].split('..')]
    yr = [int(t) for t in y.split('=')[1].split('..')]
    zr = [int(t) for t in z.split('=')[1].split('..')]
    
    rects.append(xr+yr+zr+[turn,0])
    



print('Part A Solution:', do_calc(rects[:20]))
print('Part B Solution:', do_calc(rects))