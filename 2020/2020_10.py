from utils import *

inp = sorted([int(x) for x in get_input(2020,10)])
adapter = max(inp)+3
inp = [0]+inp+[adapter]


## Part A:
ct1 = 0
ct3 = 0
for i in range(len(inp)-1):
    if inp[i+1]-inp[i]==1:
        ct1+=1
    else:
        ct3+=1

        
def ct(l):
    total = 1
    difs = [l[i+1]-l[i] for i in range(len(l)-1)]
    
    inds=[] #indices of 3 difs

    for x in range(len(difs)):
        if difs[x]==3:
            inds.append(x)
            
    difs = [inds[i+1]-inds[i] for i in range(len(inds)-1)] #differences in these indices
    
    # since differencing differences, misses start and end
    # so account for that
    difs = [inds[0]+1]+difs
    difs.append(len(l)-inds[-1]-1)
    ans=1
    for x in difs:
        if x==3:
            ans*=2
        if x==4:
            ans*=4
        if x==5:
            ans*=7
    return(ans)


print('Part A Solution:', ct1*ct3)
print('Part B Solution:', ct(inp))