from utils import *

inp = get_input(2017,13)


m = dd(int)
for x in inp:
    this = x.split(": ")
    m[int(this[0])] = int(this[1])

ans_A = 0
for x in m:
    if (x)%(2*m[x]-2)==0:
        ans_A+=x*m[x]    
    
i = 0
ans_B = 0
while True:
    total=0
    for x in m:
        if (x+i)%(2*m[x]-2)==0:
            total+=1
    if total==0:
        ans_B=i
        break
    i+=1

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)