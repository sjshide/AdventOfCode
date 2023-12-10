from utils import *

inp = get_input(2023,9)

def nextVal(L):
    lA = list(L)
    lB = list(L[::-1])
    
    lastValsA = []
    lastValsB = []    
    
    while set(lA)!=set([0]):
        lastValsA.append(lA[-1])
        lastValsB.append(lB[-1])
        lA = [lA[i+1]-lA[i] for i in range(len(lA)-1)]
        lB = [lB[i+1]-lB[i] for i in range(len(lB)-1)]
        
    return(sum(lastValsA),sum(lastValsB))

A, B = 0, 0
for x in inp:
    thisA, thisB = nextVal([int(t) for t in x.split()])
    A+=thisA
    B+=thisB

print('Part A Solution:', A)
print('Part B Solution:', B)