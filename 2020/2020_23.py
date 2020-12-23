from utils import *

inp = get_input(2020,23)
inp = [int(x) for x in inp]


# idea: care about tracking elements clockwise/counterclockwise of other elements
# relatively few of these change at each step
# removing the three changes the neighboring 6
# and adding them back elsewhere changes the neighbors for the added elements,
# plus the 3 on either side of them
# total of 18 dict updates for each move

def move(cur,mod):
    global clock
    global coclock
    dest = (cur-1)%mod
    
    while dest in clock[cur]:
        dest = (dest-1)%mod
    
    #those that change with the removal of C1,C2,C3
    c3,c2,c1 = coclock[cur]
    C1,C2,C3 = clock[cur]
    C4,C5,C6 = clock[C3]
    
    #make the changes
    clock[c2]=[c1,cur,C4]
    clock[c1]=[cur,C4,C5]
    clock[cur]=[C4,C5,C6]
    
    coclock[C4] = [c2,c1,cur]
    coclock[C5] = [c1,cur,C4]
    coclock[C6] = [cur,C4,C5]
    
    # those that change with the addition of C1,C2,C3
    d3,d2,d1 = coclock[dest]
    D1,D2,D3 = clock[dest]
    
    # make the changes
    clock[d2]=[d1,dest,C1]
    clock[d1]=[dest,C1,C2]
    clock[dest]=[C1,C2,C3]
    clock[C1] = [C2,C3,D1]
    clock[C2] = [C3,D1,D2]
    clock[C3] = [D1,D2,D3]
    coclock[C1] = [d2,d1,dest]
    coclock[C2] = [d1,dest,C1]
    coclock[C3] = [dest,C1,C2]
    coclock[D1] = [C1,C2,C3]
    coclock[D2] = [C2,C3,D1]
    coclock[D3] = [C3,D1,D2]
    
    # return the next current position
    return(clock[cur][0])


# A
l2 = list(inp)
l3 = [x-1 for x in l2]
clock = dict()
coclock = dict()
mod = len(l3)
for i in range(mod):
    clock[l3[i]] = [l3[(i+1)%mod],l3[(i+2)%mod],l3[(i+3)%mod]]
    coclock[l3[i]] = [l3[(i-3)%mod],l3[(i-2)%mod],l3[(i-1)%mod]]

curr = 0
for i in range(100):
    curr=move(curr,mod)

nex = clock[0][0]
ans_A_l = []
while nex!=0:
    ans_A_l.append(nex)
    nex=clock[nex][0]
ans_A = ''
for num in ans_A_l:
    ans_A+=str(num+1) #recorrect for -1 for modding
              

                
# B, with a bit more commentary
l2 = list(inp)+list(range(10,1_000_001)) #full list of inputs
l3 = [x-1 for x in l2]  #subtract 1 to make modding in move easier
clock = dict()         # contains for each i the 3 elements clockwise of i
coclock = dict()       # for each i the 3 elements counterclockwise of i
mod = len(l3)          # length of list

# populate the above
for i in range(mod):
    clock[l3[i]] = [l3[(i+1)%mod],l3[(i+2)%mod],l3[(i+3)%mod]]
    coclock[l3[i]] = [l3[(i-3)%mod],l3[(i-2)%mod],l3[(i-1)%mod]]

# starting position
curr = 0

# do it! takes a little under a minute
for i in range(10_000_000):
    curr=move(curr,mod)


#2 positions clockwise of 0 (1), adding back the 1s we subtracted
ans_B = (clock[0][0]+1)*(clock[0][1]+1)
                
                
print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)