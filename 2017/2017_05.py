from utils import *

inp = [int(x) for x in get_input(2017,5)]


def jumps(inst,part):
    l = list(inst)
    
    min1 = 0
    max1 = len(l)
    
    curr_ind = 0
    step_ct = 0
    
    while True:
        step_ct+=1
        
        if part=='B' and l[curr_ind]>=3:
            l[curr_ind]-=1
            off = 1
        else:
            l[curr_ind]+=1
            off = -1
        curr_ind+=(l[curr_ind]+off)
        if curr_ind<min1 or curr_ind>=max1:
            break
    return(step_ct)



print('Part A Solution:', jumps(inp,'A'))
print('Part B Solution:', jumps(inp,'B'))