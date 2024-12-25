from utils import *

inp = get_input(2024,9)

files = []
blanks = []
for i in range(len(inp)):
    if i%2:
        blanks+=[int(inp[i])]
    else:
        files+=[int(inp[i])]

# A
d = dict()
slotIx = 0
for i in range(len(files)):
    fileLen = files[i]
    for j in range(fileLen):
        d[slotIx]=i
        slotIx+=1
    if i<len(blanks):
        blankLen = blanks[i]
        for j in range(blankLen):
            d[slotIx]=-1-i
            slotIx+=1
            
A = 0
nonEmptyIx = [x for x in d if d[x]>-1]
for x in d:
    if d[x]>-1:
        A+=(x*d[x])
    else:
        if nonEmptyIx:
            lastIx = nonEmptyIx.pop(-1)
            if lastIx>x:
                d[x]=d[lastIx]
                d[lastIx]=-1
                A+=(x*d[x])
                
# B no effort made to clean this up
d = dict()
slotIx = 0
for i in range(len(files)):
    fileLen = files[i]
    for j in range(fileLen):
        d[slotIx]=i
        slotIx+=1
    if i<len(blanks):
        blankLen = blanks[i]
        for j in range(blankLen):
            d[slotIx]=-1-i
            slotIx+=1

revd = dd(list)
for x in d:
    revd[d[x]]+=[x]
    
i=len(files)-1
while i>0:
    fileLen = len(revd[i])
    check = 0
    for j in range(1,i+1):
        if check:
            break
        if len(revd[-j])>=fileLen:
            for k in range(fileLen):
                revd[i].pop(0)
                revd[i]+=[revd[-j].pop(0)]
            check=1
    i-=1
B = 0
for x in revd:
    if x>-1:
        for t in revd[x]:
            B+=t*x                

print('Part A Solution:', A)
print('Part B Solution:', B)