from utils import *

inp = int(get_input(2017,17))

def buff_A(n,steps):
    init = [0]
    ind = 0

    for t in range(1,n+1):
        ind = (ind+steps)%len(init)
        init = init[:ind+1]+[t]+init[ind+1:]
        ind = (ind+1)%len(init)

    i = init.index(t)
    
    return(init[i+1])


ind=0
zero_loc = 0
ans_B = 0
for t in range(1,50_000_000):
    ind = (ind+314)%t
    ind = (ind+1)%(t+1)
    if ind==0 and t!=1:
        zero_loc+=1
    if ind==zero_loc+1:
        ans_B=t


print('Part A Solution:', buff_A(2017,inp))
print('Part B Solution:', ans_B)