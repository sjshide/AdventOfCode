from utils import *
import numpy as np

inp = [int(x) for x in get_input(2017,6).split('\t')]

def redist(inst):
    l = np.array(inst)
    le = len(l)
    states = dict()
    steps = 0
    
    while True:
        steps+=1
        ind = l.argmax()
        val = l[ind]
        
        l[ind]=0
        
        l+=(val//le)
        rem = val%le
        
        end = min(le,rem+ind+1)
        
        l[ind+1:end]+=1
        
        rem = max((rem- (le-ind-1)),0)
        
        l[:rem]+=1

        if tuple(l) in states:
            break
        else:
            states[tuple(l)]=steps
            
    return(steps, steps-states[tuple(l)])


ans_A, ans_B = redist(inp)

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)