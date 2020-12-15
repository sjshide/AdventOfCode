from utils import *

inp = [int(t) for t in get_input(2020,15).split(',')]

## brute force again
## rewrote this function like 5 times cause I kept getting confused


def get_said(x,num):
    last_time_said = dd(int)
    said_check=set()
    last_val = -1
    
    for i in range(len(x)):
        last_time_said[x[i]]=i
        last_val = x[i]
        said_check.add(last_val)
    
    for i in range(len(x),num):
        if last_val not in said_check:
            said_check.add(last_val)
            last_time_said[last_val]=i-1
            last_val=0
        else:
            dif = i-1 - last_time_said[last_val]
            last_time_said[last_val]=i-1
            last_val=dif

    return(last_val)


print('Part A Solution:', get_said(inp,2020))
print('Part B Solution:', get_said(inp,30_000_000))