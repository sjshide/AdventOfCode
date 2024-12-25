from utils import *

inp = get_input(2024,5)

d = dd(list)
updates = []

for x in inp:
    if '|' in x:
        a,b = [int(t) for t in x.split('|')]
        d[b] = d[b]+[a]
    else:
        if len(x)>0:
            updates = updates+[[int(t) for t in x.split(',')]]

A = 0           
B = 0
for up in updates:
    check=1
    for i in range(len(up)-1):
        for j in range(i+1,len(up)):
            if up[j] in d[up[i]]:
                check=0
    A+=(check*up[len(up)//2])
    
    tempUp = list(up)
    swapIx = [1,1]
    while check==0:
        check=1
        a,b = tempUp[swapIx[0]],tempUp[swapIx[1]]
        tempUp[swapIx[0]]=b
        tempUp[swapIx[1]]=a
        for i in range(len(up)-1):
            for j in range(i+1,len(up)):
                if tempUp[j] in d[tempUp[i]]:
                    check=0
                    swapIx = [i,j]
    if tempUp!=up:
        B+=(check*tempUp[len(tempUp)//2])


print('Part A Solution:', A)
print('Part B Solution:', B)