from utils import *

inp = get_input(2024,22)

def step(n):
    M = 16777216
    n1 = n*64
    n = n^n1
    n = n%M
    n2 = n//32
    n = n^n2
    n = n%M
    n3 = n*2048
    n = n^n3
    n = n%M
    return(n)

A=0
d = dd(int)
for x in inp:
    n = int(x)
    d1 = dict()
    
    p0 = n%10    
    n = step(n)
    p1 = n%10
    n=step(n)
    p2 = n%10
    n=step(n)
    p3 = n%10
    n=step(n)
    p4 = n%10
    
    c1 = p1-p0
    c2 = p2-p1
    c3 = p3-p2
    c4 = p4-p3
    
    d1[(c1,c2,c3,c4)]=p4

    for _ in range(4,2000):
        n = step(n)
        p0,p1,p2,p3,p4=p1,p2,p3,p4,n%10
        c1,c2,c3,c4 = c2,c3,c4,p4-p3
        if (c1,c2,c3,c4) not in d1:
            d1[(c1,c2,c3,c4)]=p4
    for x in d1:
        d[x]+=d1[x]    
    A+=n
B=max([d[x] for x in d])    
    
print('Part A Solution:', A)
print('Part B Solution:', B)