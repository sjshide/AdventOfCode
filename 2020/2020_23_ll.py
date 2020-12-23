from utils import *

inp = [int(x) for x in get_input(2020,23)]


## Trying out the linked list version. Basically what I did
## (without actually thinking of it that way),
## but mine was more complicated.
## Much faster! a few seconds

def move(cur,mod):
    global ll
    
    #get moving cups
    next1 = ll[cur]
    next2 = ll[next1]
    next3 = ll[next2]
    next4 = ll[next3]
        
    dest = (cur-1)%mod
    while dest in [next1,next2,next3]:
        dest = (dest-1)%mod
    
    nd = ll[dest]
    
    ## make the move
    ll[cur] = next4
    ll[dest] = next1
    ll[next3] = nd
    
    
    return(ll[cur])


## A
l2 = list(inp)
l3 = [x-1 for x in l2]
ll = dict()
mod = len(l3)

for i in range(mod):
    ll[l3[i]] = l3[(i+1)%mod]

curr = 0
for i in range(100):
    curr=move(curr,mod)

nex = ll[0]
ans_A_l = []
while nex!=0:
    ans_A_l.append(nex)
    nex=ll[nex]
ans_A = ''
for num in ans_A_l:
    ans_A+=str(num+1)
    

## B
l2 = list(inp)+list(range(10,1_000_001)) #full list of inputs
l3 = [x-1 for x in l2]  #subtract 1 to make modding in move easier

ll = dict()
mod = len(l3)

# populate the above
for i in range(mod):
    ll[l3[i]] = l3[(i+1)%mod]

# starting position
curr = 0

# do it! takes a little under a minute
for i in range(10_000_000):
    curr=move(curr,mod)


#2 positions clockwise of 0 (1), adding back the 1s we subtracted
ans_B = (ll[0]+1)*(ll[ll[0]]+1)
print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)