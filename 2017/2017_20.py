from utils import *

inp = get_input(2017,20)

Ps = dd(list)
Vs = dd(list)
As = dd(list)

for i in range(len(inp)):
    x=inp[i]
    Ps[i],Vs[i],As[i] = [[int(t) for t in y[3:-1].split(',')] for y in x.split(', ')]

def manh(t):
    total = 0
    for ent in t:
        total+=abs(ent)
    return(total)

# A
lowest_acc = pow(10,10)
lowest_vel = pow(10,10)
ans_A = -1
for i in range(len(inp)):
    if manh(As[i])<lowest_acc:
        lowest_acc = manh(As[i])
        lowest_vel = manh(Vs[i])
        ans_A = i
    elif manh(As[i])==lowest_acc:
        if manh(Vs[i])<lowest_vel:
            lowest_vel = manh(Vs[i])
            ans_A = i

            
# B
def update(pos,vel,acc):
    for i in range(3):
        vel[i]+=acc[i]
    for i in range(3):
        pos[i]+=vel[i]
    return(pos,vel,acc)
    

valid_is = set(range(len(inp)))

# my input took 39 iterations to converge, so should be more than enough
for _ in range(500):
    for ind in valid_is:
        Ps[ind],Vs[ind],As[ind] = update(Ps[ind],Vs[ind],As[ind])
        
    pos_ct = dd(list)
    for ind in valid_is:
        pos_ct[tuple(Ps[ind])].append(ind)
    for x in pos_ct:
        if len(pos_ct[x])>1:
            for bad_ind in pos_ct[x]:
                valid_is.remove(bad_ind)
    

ans_B = len(valid_is)



print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)