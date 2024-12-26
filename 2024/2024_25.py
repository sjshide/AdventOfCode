from utils import *

inp = get_input(2024,25)

keys = []
locks = []
for i in range(0,len(inp),8):
    x = inp[i:i+7]
    if x[0]=='#####':
        loc = []
        for j in range(5):
            k=0
            while x[k+1][j]=='#':
                k+=1
            loc.append(k)
        keys.append(loc)
    else:
        x = x[::-1]
        loc = []
        for j in range(5):
            k=0
            while x[k+1][j]=='#':
                k+=1
            loc.append(k)
        locks.append(loc) 
        
A = 0
for x in keys:
    for y in locks:
        check=1
        for i in range(5):
            if x[i]+y[i]>5:
                check=0 
        A+=check

print('Part A Solution:', A)
print('Part B Solution:','PRESS THE BUTTON')